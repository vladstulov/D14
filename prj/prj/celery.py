import os
from celery import Celery
from celery.schedules import crontab
 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prj.settings')
app = Celery('prj')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.conf.beat_schedule = {
    'weekly_subscribe': {
        'task': 'newsapp.tasks.weekly_mail',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
        #'schedule': crontab(),
    },
}
app.autodiscover_tasks()

