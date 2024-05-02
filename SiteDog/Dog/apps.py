from django.apps import AppConfig


class DogConfig(AppConfig):
    verbose_name = 'Известные Породы собак'
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Dog'
