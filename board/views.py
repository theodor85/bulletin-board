from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Board

def index(request):
    ads = Board.objects.order_by('-date')
    return render(request, 'board/index.html', {'ads': ads})

def login(request):
    return render(request, 'board/login.html', {})

def edit(request):
    return render(request, 'board/edit.html', {})

def add(request):
    return render(request, 'board/add.html', {})

def add_item(request):
    board = Board()
    board.author = request.user
    board.head = request.POST['head']
    board.price = request.POST['price']
    board.text = request.POST['text']
    board.save()
    return render(request, 'board/add_success.html', {})

def delete(request):
    return render(request, 'board/delete_success.html', {})

class RegisterFormView(FormView):
    
    form_class = UserCreationForm
    success_url = '/board/login/'
    template_name = 'board/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
