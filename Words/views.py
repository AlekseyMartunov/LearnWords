from django.http import HttpResponse
from django.views.generic import ListView, DetailView, TemplateView
from .models import Words
from .forms import AddWordsForm
import json


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


class AddWords(TemplateView):
    """Класс для записи новых слов в базу"""
    template_name = "Words/AddWords.html"

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












