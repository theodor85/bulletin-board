from django.urls import path

from .views import index, register, login, BoardCreateView, edit

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('add/', BoardCreateView.as_view(), name='add'),
    path('edit/', edit, name='edit'),
]