from flask import Blueprint, render_template

from .forms import LoginForm

from app.models import User


auth = Blueprint('auth', __name__, template_folder='templates/auth')

config_login = {
    'login_view': 'auth.login',
    'login_message': 'Ви маєте зайти!',
    'login_message_category': 'warning'
}

from . import routes


@auth.app_context_processor
def auth_context():
    login_form = LoginForm()

    context = {
        'header_form': login_form
    }

    return context


def load_user(user_id):
        return User.query.get(user_id)
