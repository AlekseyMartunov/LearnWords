# Generated by Django 4.1.3 on 2022-11-16 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Words', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='words',
            name='slug',
            field=models.SlugField(null=True),
        ),
        migrations.AlterField(
            model_name='words',
            name='correct',
            field=models.PositiveBigIntegerField(verbose_name='Количество правильных ответов'),
        ),
        migrations.AlterField(
            model_name='words',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Дата создания'),
        ),
        migrations.AlterField(
            model_name='words',
            name='errors',
            field=models.PositiveBigIntegerField(verbose_name='Ошибки'),
        ),
    ]
