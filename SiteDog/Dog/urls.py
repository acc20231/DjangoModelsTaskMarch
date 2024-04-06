from django.urls import path, register_converter
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, 'year4')

urlpatterns = [
    path('', views.index, name='home'),
    path('Dreed/<int:dreed_id>/', views.categories, name='treed_id'),
    path('Dreed/<slug:dreed_slug>/', views.categories_slug, name='treed'),
    path('archive/<year4:year>/', views.archive, name='archive'),
]