from flask import Flask

from .extentions import db
from .commands import create_tables
from app.auth import auth


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # Extentions
    db.init_app(app)

    # Commands
    app.cli.add_command(create_tables)

    # Bluprints
    app.register_blueprint(auth)

    with app.app_context():

        # Routes for main part of app.
        from . import routes

    return app
