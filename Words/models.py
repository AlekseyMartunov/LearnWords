from django.template.defaultfilters import slugify
from django.db import models
from django.urls import reverse


class Words(models.Model):
    """Класс для хранения информации о слове"""
    name_rus = models.CharField(max_length=100)
    name_eng = models.CharField(max_length=100)
    errors = models.PositiveBigIntegerField("Ошибки", default=0)
    correct = models.PositiveBigIntegerField("Количество правильных ответов", default=0)
    created = models.DateTimeField("Дата создания", auto_now_add=True)
    last_repeat = models.DateTimeField(auto_now=True)
    user_ip = models.CharField(max_length=15, null=False)

    def get_absolute_url(self):
        return reverse("detail_view", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name_rus}: {self.name_eng}"

    class Meta:
        verbose_name = "Слово"
        verbose_name_plural = "Слова"


