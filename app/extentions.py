from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate
from celery import Celery


db = SQLAlchemy()
login = LoginManager()
migrate = Migrate()
celery = Celery('app')
