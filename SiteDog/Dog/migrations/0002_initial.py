# Generated by Django 4.2.1 on 2024-05-10 14:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Dog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='posts', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dog',
            name='cat',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Dog.category', verbose_name='Порода'),
        ),
        migrations.AddIndex(
            model_name='dog',
            index=models.Index(fields=['-time_create'], name='Dog_dog_time_cr_375f1a_idx'),
        ),
    ]