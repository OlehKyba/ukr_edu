from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from celery import Celery


db = SQLAlchemy()
login = LoginManager()
celery = Celery('app')
