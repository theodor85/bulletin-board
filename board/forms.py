from django.forms import ModelForm, CharField, PasswordInput

from .models import Board

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ('head', 'text', 'price', 'author')
