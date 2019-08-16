from flask import Flask

from .extentions import db
from .commands import create_tables, drop_tables, create_test_db
from app.auth import auth


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # Extentions
    db.init_app(app)

    # Commands
    app.cli.add_command(create_tables)
    app.cli.add_command(drop_tables)
    app.cli.add_command(create_test_db)

    # Bluprints
    app.register_blueprint(auth)

    with app.app_context():

        # Routes for main part of app.
        from . import routes

    return app
