from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))



class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=Dog.Status.PUBLISHED)





class Dog(models.Model):
    class Status(models.IntegerChoices):
        DRAFT = 0, 'Черновик'
        PUBLISHED = 1, 'Опубликовано'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')
    content = models.TextField(blank=True, verbose_name='Краткое описание')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name='Время изменения')
    is_published = models.BooleanField(choices=tuple(map(lambda x: (bool(x[0]), x[1]), Status.choices)),
                                       default=Status.DRAFT, verbose_name='Статус')
    objects = models.Manager()
    published = PublishedManager()
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Порода')

    author = models.ForeignKey(get_user_model(), on_delete=models.SET_NULL,
                               related_name='posts', null=True, default=None)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Породы собак'
        verbose_name_plural = 'Породы собак'
        ordering = ['-time_create']
        indexes = [
            models.Index(fields=['-time_create'])

        ]

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name
