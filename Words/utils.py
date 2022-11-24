from .models import Words

menu = ({"name": "Домашняя страница", "url": "home"},
        {"name": "Добавить слова", "url": "add_words"},
        {"name": "Статистика", "url": "statistics"},)


class DataMixin:
    """Класс для устранения дублирования кода,
    Тут содержится общая информация"""
    def get_user_context(self, **kwargs):
        context = kwargs
        context["menu"] = menu
        return context



