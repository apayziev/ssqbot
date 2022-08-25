# Generated by Django 4.0.7 on 2022-08-22 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='title_ru',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='title_ru',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='condition',
            old_name='title_ru',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='title_ru',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='answer',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='category',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='condition',
            name='title_uz',
        ),
        migrations.RemoveField(
            model_name='question',
            name='title_uz',
        ),
    ]
