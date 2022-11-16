from django.apps import AppConfig


class WordsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Words'

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"
