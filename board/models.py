from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    ''' Класс, отображающий таблицу БД со списком объявлений '''
    date =  models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    head = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст объявления')
    price = models.FloatField(verbose_name='Цена')
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False) 

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-date']

    def __str__(self):
        return self.head
