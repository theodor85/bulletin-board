from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, login, BoardCreateView, edit, RegisterFormView

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('add/', BoardCreateView.as_view(), name='add'),
    path('edit/', edit, name='edit'),
    path('logout/', LogoutView.as_view(), name='logout')
]