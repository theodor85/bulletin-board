from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from django.views.generic import View
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import BoardForm
from django.core.paginator import Paginator

from .models import Board

def index(request):
    ''' Первая страница выводит все объявления. Использует пагинатор '''

    ads = Board.objects.order_by('-date')
    paginator = Paginator(ads, 5)

    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1

    page = paginator.get_page(page_num)
    context = {'ads': page.object_list, 'page':page, 'page_range':range(1, paginator.num_pages+1)}
    return render(request, 'board/index.html', context)


def login(request):
    return render(request, 'board/login.html', {})

class EditDeleteBase(UserPassesTestMixin, View):
    """Базовый класс для контроллеров BoardEdit и BoardDelete."""

    login_url = 'login' # для класса UserPassesTestMixin - URL переадресации
                        # на страницу входа
    def test_func(self):
        ''' Функция для предоставления доступа к элементу только
        автору и администратору. '''

        item = get_object_or_404(Board, pk=self.kwargs['item_id'])

        if item.author == self.request.user:
            return True
        elif self.request.user.is_superuser:
            return True
        else:
            return False


class BoardEdit(EditDeleteBase):
    """Контроллер, отвечающий за редактирование элемента."""

    def get(self, request, item_id):
        ''' При GET-запросе возвращаем страницу с формой редактирования элемента. '''
        item = get_object_or_404(Board, pk=item_id)
        data = {}
        data['price'] = item.price
        data['head'] = item.head
        data['text'] = item.text
        form = BoardForm(data)
        return render(request, 'board/edit.html', {'form':form})

    def post(self, request, item_id):
        ''' При POST-запросе сохраняем измененияв БД, предварительно сделав валидацию. '''
        form = BoardForm(request.POST)

        if form.is_valid():
            item = get_object_or_404(Board, pk=item_id)
            item.head = request.POST['head']
            item.price = float(request.POST['price'])
            item.text = request.POST['text']
            item.save()
            return render(request, 'board/edit_success.html', {})

        return render(request, 'board/edit.html', {'form': form})


class BoardAdd(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        form = BoardForm()
        return render(request, 'board/add.html', {'form': form})

    def post(self, request):
        form = BoardForm(request.POST)

        form.fields['head'].widget.attrs.update({'class': 'form-control'})
        form.fields['text'].widget.attrs.update({'class': 'form-control'})
        form.fields['price'].widget.attrs.update({'class': 'form-control'})

        if form.is_valid():
            new_board = form.save(commit=False)
            new_board.author = request.user
            new_board.save()
            return render(request, 'board/add_success.html', {})

        return render(request, 'board/add.html', {'form': form})

class BoardDelete(EditDeleteBase):
    """Контроллер, отвечающий за удаление элемента."""
    def get(self, request, item_id):
        item = get_object_or_404(Board, pk=item_id)
        item.delete()
        return render(request, 'board/delete_success.html', {})


class RegisterFormView(FormView):

    form_class = UserCreationForm
    success_url = '/board/login/'
    template_name = 'board/register.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
