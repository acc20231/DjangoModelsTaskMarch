# Generated by Django 4.2.1 on 2024-04-28 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Dog', '0003_alter_dog_slag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dog',
            old_name='slag',
            new_name='slug',
        ),
    ]
