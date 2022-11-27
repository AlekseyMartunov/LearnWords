from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView, View
from django.db.models import F
import json

from .models import Words
from .forms import AddWordsForm
from .utils import DataMixin, QuestionMaker


class HomePage(DataMixin, ListView):
    """Класс для отображения главной страницы"""
    model = Words
    template_name = "Words/HomePage.html"
    context_object_name = "words"

    def get(self, request, *args, **kwargs):
        """Переопределение функции get для получения слов, отфильтрованных по ip"""
        ip = self.get_client_ip(request)
        words = Words.objects.filter(user_ip=ip)
        user_context = self.get_user_context(Title="Главная")
        user_context["selected"] = 1
        user_context["words"] = words
        return render(request, self.template_name, context=user_context)


class WordDetail(DataMixin, DetailView):
    """Класс для отображения детальной информации о слове"""
    model = Words
    slug_field = "pk"
    template_name = "Words/DetailPage.html"
    context_object_name = "word"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="О слове...")
        return {**context, **user_context}

    def post(self, request, pk):
        Words.objects.get(pk=pk).delete()
        return redirect('/', permanent=True)


class AddWords(DataMixin, TemplateView):
    """Класс для записи новых слов в базу"""
    template_name = "Words/AddWords.html"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user_context = self.get_user_context(Title="Добавить запись")
        user_context["selected"] = 2
        return {**context, **user_context}

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

    def get(self, request, *args, **kwargs):
        """Переопределение функции get для получения слов, отфильтрованных по ip"""
        ip = self.get_client_ip(request)
        words = Words.objects.filter(user_ip=ip)
        user_context = self.get_user_context(Title="Учеба")
        user_context["selected"] = 3
        user_context["words"] = words
        return render(request, self.template_name, context=user_context)

    def post(self, request):
        data = json.loads(request.body.decode("utf-8"))
        if "results" in data:
            for key, value in data["results"].items():
                word = Words.objects.get(pk=int(key))
                if value:
                    word.correct = F("correct") + 1
                else:
                    word.errors = F("errors") + 1
                word.save()
            return HttpResponse(status=200)

        else:
            ip = self.get_client_ip(request)
            words = Words.objects.filter(user_ip=ip)
            flag = data["language"] == "eng"
            test = QuestionMaker(flag, words)
            questions = test.get_questions()
            return JsonResponse(questions, safe=False)











