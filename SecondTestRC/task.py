from celery import shared_task

@shared_task
def add_bool(value):
    from SecondTestRC.views import SecondHomePageView
    SecondHomePageView().get_bool_second(value)
    result = 123 if value else None
    # результат возвращается в автоматически созданную очередь на изначальную ручку отправителя
    # после очередь ответа удаляется см. файл custom_backend
    return result

@shared_task
def add_cost(cost):
    from SecondTestRC.views import SecondHomePageView
    SecondHomePageView().get_cost_second(cost)
    return {'some_json_data':{'поздравляю':'ответ','успешно':'получен'}}