import os
from app.utils import di_config


SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
SECRET_KEY = os.environ.get('SECRET_KEY')
SQLALCHEMY_TRACK_MODIFICATIONS = False

S3_IMG_BUCKET = os.environ.get('S3_POST_IMG_BUCKET')

CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_ACCEPT_CONTENT = ['pickle']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'


di_config.update({
    'aws': {
        'preview_bucket': S3_IMG_BUCKET
    }
})
