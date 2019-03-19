from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView, FormView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm

from .models import Board
from .forms import BoardForm

def index(request):
    ads = Board.objects.order_by('-date')
    return render(request, 'board/index.html', {'ads': ads})

def login(request):
    return render(request, 'board/login.html', {})

def edit(request):
    return render(request, 'board/edit.html', {})

class BoardCreateView(LoginRequiredMixin, CreateView):
    template_name = 'board/add.html'
    form_class = BoardForm
    success_url = reverse_lazy('index')
    login_url = '/board/login/'

class RegisterFormView(FormView):
    
    form_class = UserCreationForm
    success_url = '/board/login/'
    template_name = 'board/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
