from flask import has_app_context
from celery import Celery
from .settings import CELERY_BROKER_URL


def make_celery(app_name):
    celery = Celery(app_name, broker=CELERY_BROKER_URL)

    celery.conf['CELERY_ACCEPT_CONTENT'] = ['pickle']
    celery.conf['CELERY_TASK_SERIALIZER'] = 'pickle'
    celery.conf['CELERY_RESULT_SERIALIZER'] = 'pickle'

    return celery


def init_celery(celery, app):
    celery.conf.update(app.config)
    TaskBase = celery.Task

    class ContextTask(TaskBase):

        def __call__(self, *args, **kwargs):
            if has_app_context():
                return TaskBase.__call__(self, *args, **kwargs)

            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)

    celery.Task = ContextTask
