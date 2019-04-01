from django import forms
from .models import Board
from django.core.exceptions import ValidationError

class BoardForm(forms.ModelForm):

    class Meta:
        model = Board
        fields = ['head','text', 'price']

    def clean_price(self):

        try:
            cleaned_price = float(self.cleaned_data['price'])
        except:
            raise ValidationError('Не удалось преобразовать цену в число!')

        if cleaned_price < 0:
            raise ValidationError('Цена не может быть отрицательной!')

        return cleaned_price
