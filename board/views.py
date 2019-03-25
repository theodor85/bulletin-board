from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import BoardForm

from .models import Board

def index(request):
    ads = Board.objects.order_by('-date')
    return render(request, 'board/index.html', {'ads': ads})

def login(request):
    return render(request, 'board/login.html', {})

@login_required(login_url='/board/login/')
def edit(request, item_id):
    item = get_object_or_404(Board, pk=item_id)
    return render(request, 'board/edit.html', {'item':item})

def edit_item(request, item_id):
    item = get_object_or_404(Board, pk=item_id)
    item.head = request.POST['head']
    item.price = float(request.POST['price'])
    item.text = request.POST['text']
    item.save()
    return render(request, 'board/edit_success.html', {})

class BoardAdd(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        form = BoardForm()
        return render(request, 'board/add.html', {'form': form})

    def post(self, request):
        form = BoardForm(request.POST)

        if form.is_valid():
            new_board = form.save(commit=False)
            new_board.author = request.user
            new_board.save()
            return render(request, 'board/add_success.html', {})

        return render(request, 'board/add.html', {'form': form})

class BoardDelete(UserPassesTestMixin, View):
    """docstring for BoardDelete."""
    def get(self, request, item_id):
        item = get_object_or_404(Board, pk=item_id)
        item.delete()
        return render(request, 'board/delete_success.html', {})

    def test_func(self):
        item = get_object_or_404(Board, pk=self.kwargs['item_id'])
        if item.author == self.request.user:
            return True
        elif self.request.user.is_superuser:
            return True
        else:
            return False

class RegisterFormView(FormView):

    form_class = UserCreationForm
    success_url = '/board/login/'
    template_name = 'board/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
