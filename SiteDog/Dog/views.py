from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.template.loader import render_to_string

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},
        {'title': 'Войти', 'url_name': 'login'},
]

cats_db = [
    {'id': 1, 'name': 'Маленькие'},
    {'id': 2, 'name': 'Средние'},
    {'id': 3, 'name': 'Большие'}
]

data_db = [
    {'id': 1, 'title': 'Порода пастушьих собак: Корги', 'content': 'Описание породы', 'is_published': True},
    {'id': 2, 'title': 'Джек-рассел-терьер', 'content': 'Описание породы', 'is_published': False},
    {'id': 3, 'title': 'Немецкая овчарка', 'content': 'Описание породы', 'is_published': True},
]


def index(request):

    date = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selectad': 0,
    }
    return render(request, 'Dog/index.html', context=date)

def about(request):
    return render(request, 'Dog/about.html', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_id):
    return HttpResponse(f'Отображение статьи с id {post_id}')

def login(request):
    return HttpResponse('Авторизация')

def addpage(request):
    return HttpResponse('Добавление статьи')

def contact(request):
    return HttpResponse('Обратная связь')

def show_category(request, cat_id):
    date = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': data_db,
        'cat_selectad': cat_id,
    }
    return index(request)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
