from flask import Flask

from .extentions import db, login
from .commands import create_tables, drop_tables, create_test_db

from app.auth import auth, load_user, config_login, unauthorized_handler
from app.posts import posts


def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    # Extentions
    db.init_app(app)
    login.init_app(app)

    # Flask-Login config
    login.user_loader(load_user)
    login.unauthorized_handler(unauthorized_handler)
    login.login_view = config_login['login_view']
    login.login_message = config_login['login_message']
    login.login_message_category = config_login['login_message_category']

    # Commands
    app.cli.add_command(create_tables)
    app.cli.add_command(drop_tables)
    app.cli.add_command(create_test_db)

    # Bluprints
    app.register_blueprint(auth)
    app.register_blueprint(posts, url_prefix='/posts')
    with app.app_context():
        # Routes for main part of app.
        from . import routes

    return app
