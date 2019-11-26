from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .celery_utils import make_celery


db = SQLAlchemy()
login = LoginManager()
celery = make_celery('app')
