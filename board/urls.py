from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, login, add, edit, RegisterFormView, add_item, delete

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('add/', add, name='add'),
    path('add_item/', add_item, name='add_item'),
    path('edit/', edit, name='edit'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete/', delete, name='delete'),
]