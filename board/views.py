from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Board
from .forms import BoardForm

def index(request):
    ads = Board.objects.order_by('-date')
    return render(request, 'board/index.html', {'ads': ads})

def register(request):
    return render(request, 'board/register.html', {})

def login(request):
    return render(request, 'board/login.html', {})

def edit(request):
    return render(request, 'board/edit.html', {})

class BoardCreateView(CreateView):
    template_name = 'board/add.html'
    form_class = BoardForm
    success_url = reverse_lazy('index')

    # def get_context_data(self, **kwargs):
    #     content = super().get_context_data(**kwargs)
    #     return content

