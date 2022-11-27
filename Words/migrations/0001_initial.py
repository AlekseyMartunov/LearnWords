# Generated by Django 4.1.3 on 2022-11-27 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rus', models.CharField(max_length=100)),
                ('name_eng', models.CharField(max_length=100)),
                ('errors', models.PositiveBigIntegerField(default=0, verbose_name='Ошибки')),
                ('correct', models.PositiveBigIntegerField(default=0, verbose_name='Количество правильных ответов')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('last_repeat', models.DateTimeField(auto_now=True)),
                ('user_ip', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
            },
        ),
    ]
