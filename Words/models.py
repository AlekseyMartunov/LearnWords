from django.db import models
from django.contrib.auth.models import User


class Words(models.Model):
    """Клас для хранения информации о слове"""
    name_rus = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    errors = models.PositiveBigIntegerField("Ошибки")
    correct = models.PositiveBigIntegerField("Количество правильных ответов")
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    last_repeat = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name_rus}: {self.name_eng}"

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"


