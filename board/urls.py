from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, login, add, edit, RegisterFormView, add_item, delete, edit_item, BoardAdd

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('add/', BoardAdd.as_view(), name='add'),
    path('add_item/', add_item, name='add_item'),
    path('edit/', edit, name='edit'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete/<int:item_id>/', delete, name='delete'), 
    path('edit/<int:item_id>/', edit, name='edit'),
    path('edit_item/<int:item_id>/', edit_item, name='edit_item'),
]