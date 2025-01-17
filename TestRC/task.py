from TestRC.models import Receiver
from celery import shared_task

@shared_task
def add_name(name):
    Receiver.objects.create(name=name, age=18)
    # результат возвращается в автоматически созданную очередь на изначальную ручку отправителя
    # после очередь ответа удаляется см. файл custom_backend
    return 'Имя успешно записано в базу данных'

@shared_task
def add_age(age):
    Receiver.objects.create(age=age)
    return 'Возраст успешно записано в базу данных'