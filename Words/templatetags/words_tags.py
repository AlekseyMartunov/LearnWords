from datetime import datetime
from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def time_difference(context):
    word = context['word'].created
    was_created = datetime(word.year, word.month, word.day, word.hour, word.minute)
    delta = datetime.now() - was_created

    days, seconds = delta.days, delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    return f"Дней: {days}, Часов:{hours}, Минут: {minutes}"