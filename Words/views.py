from django.http import HttpResponse
from django.http import JsonResponse
from django.views.generic import ListView, DetailView, TemplateView
import json

from .models import Words
from .forms import AddWordsForm
from .utils import DataMixin, QuestionMaker


class HomePage(DataMixin, ListView):
    """Класс для отображения главной страницы"""
    model = Words
    template_name = "Words/HomePage.html"
    context_object_name = "words"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="Главная")
        return {**context, **user_context}


class WordDetail(DataMixin, DetailView):
    """Класс для отображения детальной информации о слове"""
    model = Words
    slug_field = "slug"
    template_name = "Words/DetailPage.html"
    context_object_name = "word"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="О слове...")
        return {**context, **user_context}


class Statistics(DataMixin, TemplateView):
    """Класс для отображения статистики"""
    template_name = "Words/Statistics.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="Статистика")
        return {**context, **user_context}


class AddWords(DataMixin, TemplateView):
    """Класс для записи новых слов в базу"""
    template_name = "Words/AddWords.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="Добавить запись")
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


class Study(DataMixin, TemplateView):
    """Класс для рендеринга вопросов"""
    template_name = "Words/Study.html"

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="Учеба")
        return {**context, **user_context}

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        if "results" in data:
            for key, value in data["results"].items():
                word = Words.objects.get(pk=int(key))
                if value:
                    word.correct += 1
                else:
                    word.errors += 1
                word.save()
            return HttpResponse(status=200)

        else:
            ip = self.get_client_ip(request)
            words = Words.objects.filter(user_ip=ip)
            flag = data["language"] == "eng"
            test = QuestionMaker(flag, words)
            questions = test.get_questions()
            return JsonResponse(questions, safe=False)











