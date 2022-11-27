from datetime import datetime
from django import template


register = template.Library()


@register.simple_tag(takes_context=True)
def time_difference(context):

    word = context['word'].created
    was_created = datetime(word.year, word.month, word.day, word.hour, word.minute, word.second)
    delta = datetime.utcnow() - was_created

    days, seconds = delta.days, delta.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60

    if not hours:
        return f"Минут: {minutes}, Секунд: {delta.seconds % 60}"

    if not days:
        return f"Часов:{hours}, Минут: {minutes}"

    return f"Дней: {days}, Часов:{hours}"