from django import template
from django.utils.safestring import mark_safe
import markdown

register = template.Library()

@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))

@register.filter(name='reading_time')
def reading_time(text):
    words_per_minute = 200
    word_count = len(text.split())
    minutes = word_count // words_per_minute
    return max(1, minutes)  # Return at least 1 minute 