from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .celery_utils import make_celery
from .utils.services import Services


db = SQLAlchemy()
login = LoginManager()
celery = make_celery('app')
preview_storage = Services.preview()
