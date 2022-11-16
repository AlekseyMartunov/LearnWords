from django.contrib import admin
from .models import Words


@admin.register(Words)
class WordsAdmin(admin.ModelAdmin):
    list_display = ('name_rus', 'name_eng', 'errors', 'correct', 'created', 'user')
    readonly_fields = ('errors', 'correct', 'created',)
    prepopulated_fields = {'slug': ('name_eng',)}

