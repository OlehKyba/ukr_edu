from app import create_app
from app.extentions import celery


if __name__ == '__main__':
    app = create_app(celery=celery)
    app.run()
