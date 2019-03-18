from django.db import models

class Board(models.Model):
    ''' Класс, отображающий таблицу БД со списком объявлений '''
    date =  models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    head = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(verbose_name='Текст объявления')
    price = models.FloatField(verbose_name='Цена')

    class Meta:
        verbose_name_plural = 'Объявления'
        verbose_name = 'Объявление'
        ordering = ['-date']

    def __repr__(self):
        return self.head
    
