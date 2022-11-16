from django.views.generic import ListView, DetailView, View
from .models import Words


class HomePage(ListView):
    """Класс для отображения главной страницы"""
    model = Words
    template_name = "Words/HomePage.html"
    context_object_name = "words"


class WordDetail(DetailView):
    """Класс для отображения детальной информации о слове"""
    model = Words
    slug_field = "slug"
    template_name = "Words/DetailPage.html"
    context_object_name = "word"


class AddWords(DetailView):
    """Класс для записи новых слов в базу"""
    model = Words
    template_name = "Words/AddWords.html"

