from django import template
import datetime
register = template.Library()
from django.utils import timezone

@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag
def get_hour():
    return timezone.localtime(timezone.now()).hour