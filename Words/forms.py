from django import forms
from .models import Words


class AddWordsForm(forms.ModelForm):
    """Форма для добавления слов в базу"""
    class Meta:
        model = Words
        fields = ("name_rus", "name_eng", "user_ip")



