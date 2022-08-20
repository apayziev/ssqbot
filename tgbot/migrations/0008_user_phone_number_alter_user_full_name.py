# Generated by Django 4.0.7 on 2022-08-20 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tgbot', '0007_user_full_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone_number',
            field=models.CharField(default=1, max_length=13),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='full_name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
