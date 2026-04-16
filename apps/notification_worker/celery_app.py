import os
from celery import Celery

# Настройки брокера (RabbitMQ)
app = Celery(
    'notification_worker',
    broker='pyamqp://guest@localhost//',
    backend='rpc://'
)

app.conf.update(
    task_serializer='json',
    accept_content=['json'],
    result_serializer='json',
    timezone='UTC',
    enable_utc=True,
)