# Generated by Django 4.0.7 on 2022-08-22 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_alter_category_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='title_r',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='title_u',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_r',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='title_u',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='condition',
            name='title_r',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='condition',
            name='title_u',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='title_r',
            field=models.CharField(max_length=256, null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='title_u',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
