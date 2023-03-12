from django.dispatch import receiver
from django.template.loader import render_to_string

from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from newsapp.models import News
from django.db.models.signals import post_save, m2m_changed
from .tasks import send_notifications



@receiver(post_save, sender = News)
def notify_about_new_news(sender, instance, created, **kwargs):
    if created:
        category = instance.category
        subscribers: list[str] = []
        subscribers = category.subscribers.all()
        subscribers = [s.email for s in subscribers]
        send_notifications.delay(instance.text, instance.pk, instance.title, subscribers)

