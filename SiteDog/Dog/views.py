from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView

# from .forms import AddPostForm
from .models import Dog

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь', 'url_name': 'contact'},

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


@login_required
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


@login_required
def addpage(request):
    return HttpResponse('Добавление статьи')


@login_required
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


class AddPage(PermissionRequiredMixin, LoginRequiredMixin, CreateView):
    # form_class = AddPostForm
    # template_name = 'Dog/addpage.html'
    # title_page = 'Добавление статьи'
    # permission_required = 'dog.add_women' # <приложение>.<действие>_<таблица>

    def form_valid(self, form):
        w = form.save(commit=False)
        w.author = self.request.user
        return super().form_valid(form)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
