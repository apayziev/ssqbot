# Generated by Django 4.0.7 on 2022-08-23 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0006_answer_title_uz_category_title_uz_condition_title_uz_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=2048)),
                ('min_score', models.IntegerField()),
                ('max_score', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Result',
                'verbose_name_plural': 'Results',
            },
        ),
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Answer', 'verbose_name_plural': 'Answers'},
        ),
        migrations.AlterModelOptions(
            name='condition',
            options={'verbose_name': 'Condition', 'verbose_name_plural': 'Conditions'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AddField(
            model_name='answer',
            name='score',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='answer',
            name='title',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='answer',
            name='title_ru',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='answer',
            name='title_uz',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_ru',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='title_uz',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='title',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='condition',
            name='title_ru',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='condition',
            name='title_uz',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title',
            field=models.CharField(max_length=1024),
        ),
        migrations.AlterField(
            model_name='question',
            name='title_ru',
            field=models.CharField(max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='title_uz',
            field=models.CharField(max_length=1024, null=True),
        ),
    ]
