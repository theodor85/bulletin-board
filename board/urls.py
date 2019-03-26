from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import index, login, RegisterFormView
from .views import BoardAdd, BoardDelete, BoardEdit

urlpatterns = [
    path('register/', RegisterFormView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('add/', BoardAdd.as_view(), name='add'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('delete/<int:item_id>/', BoardDelete.as_view(), name='delete'),
    path('edit/<int:item_id>/', BoardEdit.as_view(), name='edit'),
]
