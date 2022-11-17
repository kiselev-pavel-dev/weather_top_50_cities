import os

from celery import Celery

from . settings import PERIOD

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'weather.settings')
app = Celery('weather')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
app.conf.beat_schedule = {
    'collector-every-1-hours': {
        'task': 'top_50.tasks.collector',
        'schedule': PERIOD,
    },
}
app.conf.enable_utc = False
