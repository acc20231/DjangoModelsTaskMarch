from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.template.loader import render_to_string

from .models import Dog

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


def index(request):
    posts = Dog.published.all()
    date = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts,
        'cat_selectad': 0,
    }
    return render(request, 'Dog/index.html', context=date)

def about(request):
    return render(request, 'Dog/about.html', {'title': 'О сайте', 'menu': menu})

def show_post(request, post_slug):
    post = get_object_or_404(Dog, slug=post_slug)

    date = {
        'title': post.title,
        'menu': menu,
        'post': post,
        'cat_selectad': 1,
    }

    return render(request, 'Dog/post.html', date)

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
