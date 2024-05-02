from django import template
from users.migrations import Dog as views

register = template.Library()

@register.simple_tag
def get_menu():
    return views.menu
@register.simple_tag()
def get_categories():
    return views.cats_db

@register.inclusion_tag('Dog/list_categories.html')
def show_categories(cat_selectad=0):
    cats = views.cats_db
    return {'cats': cats, 'cat_selectad': cat_selectad}