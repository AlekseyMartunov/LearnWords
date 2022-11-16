# Generated by Django 4.1.3 on 2022-11-16 12:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_rus', models.CharField(max_length=100)),
                ('name_eng', models.CharField(max_length=100)),
                ('errors', models.PositiveBigIntegerField(verbose_name='Сколько раз пользователь ошибся на этом слове')),
                ('correct', models.PositiveBigIntegerField(verbose_name='Сколько раз пользователь правильно угадал слово')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('last_repeat', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Слово',
                'verbose_name_plural': 'Слова',
            },
        ),
    ]