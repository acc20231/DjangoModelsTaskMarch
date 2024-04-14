from django import template
import Dog.views as views

register = template.Library()

@register.simple_tag()
def get_categories():
    return views.cats_db

@register.inclusion_tag('Dog/list_categories.html')
def show_categories(cat_selectad=0):
    cats = views.cats_db
    return {'cats': cats, 'cat_selectad': cat_selectad}