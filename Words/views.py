from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
import json

from .models import Words
from .forms import AddWordsForm
from .utils import DataMixin


class HomePage(DataMixin, ListView):
    """Класс для отображения главной страницы"""
    model = Words
    template_name = "Words/HomePage.html"
    context_object_name = "words"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="Home Page")
        return {**context, **user_context}


class WordDetail(DataMixin, DetailView):
    """Класс для отображения детальной информации о слове"""
    model = Words
    slug_field = "slug"
    template_name = "Words/DetailPage.html"
    context_object_name = "word"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="Home Page")
        return {**context, **user_context}


class Statistics(DataMixin, TemplateView):
    """Класс для отображения статистики"""
    template_name = "Words/Statistics.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="Home Page")
        return {**context, **user_context}


class AddWords(DataMixin, TemplateView):
    """Класс для записи новых слов в базу"""
    template_name = "Words/AddWords.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="Home Page")
        return {**context, **user_context}

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        data["user_ip"] = self.get_client_ip(request)
        form = AddWordsForm(data)
        if form.is_valid():
            form.save()
            return HttpResponse(status=200)
        else:
            return HttpResponse(status=400)












