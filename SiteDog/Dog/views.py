from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse


# Create your views here.

def index(request):
    return HttpResponse('Страница приложения Dogs')


def categories(request, dreed_id):
    return HttpResponse(f'<h1>Страница пород Dogs</h1><p>id: {dreed_id}</p>')


def categories_slug(request, dreed_slug):
    if request.POST:
        print(request.POST)
    return HttpResponse(f'<h1>Страница пород Dogs</h1><p>slug: {dreed_slug}</p>')


def archive(request, year):
    if year > 2024:
        uri = reverse('treed', args=('Corgi',))
        return redirect(uri)
        # raise Http404()
    return HttpResponse(f'<h1>Архив по годам</h1><p>yaer: {year}</p>')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
