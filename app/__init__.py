from flask import Flask

from .extentions import db


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # Extentions
    db.init_app(app)

    return app
