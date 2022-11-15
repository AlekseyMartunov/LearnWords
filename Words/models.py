from django.db import models


class Words(models.Model):
    """Клас для хранения информации о слове"""
    name_rus = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    errors = models.PositiveBigIntegerField("Сколько раз пользователь ошибся на этом слове")
    correct = models.PositiveBigIntegerField("Сколько раз пользователь правильно угадал слово")
    created = models.DateTimeField(auto_now_add=True)
    last_repeat = models.DateTimeField(auto_now=True)
    user_ip = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name_rus}: {self.name_eng}"

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"


