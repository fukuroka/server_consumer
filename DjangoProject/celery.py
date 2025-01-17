import os

from celery import Celery
from kombu import Queue, Exchange

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DjangoProject.settings')

app = Celery('DjangoProject')


# создаем 2 очереди и привязываем их к бирже BaseExchange
app.conf.task_queues = (
    Queue('queue1',
          Exchange('BaseExchange', type='topic'),
          routing_key='SecondTestRC.*', max_priority=9 # routing_key - ключ маршрутизации, определяющий в какую очередь отправить сообщение
    ),
    Queue('queue2',
          Exchange('BaseExchange', type='topic'),
          routing_key='TestRC.*', max_priority=9 # max_priority - указание максимального приоритета задач в очереди
          ),
)

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()