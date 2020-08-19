from app import create_app
from app.extentions import celery
from app.utils import init_celery


app = create_app()
init_celery(celery, app)
