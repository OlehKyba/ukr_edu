from app import create_app
from app.extentions import celery, db
from app.celery_utils import init_celery


app = create_app()
init_celery(celery, app)
