from flask import Blueprint, render_template, flash, redirect, url_for, request

from .forms import LoginForm

from app.models import User


auth = Blueprint('auth', __name__, template_folder='templates/auth')

from . import routes

config_login = {
    'login_view': 'auth.login',
    'login_message': 'Ви маєте зайти!',
    'login_message_category': 'warning'
}


@auth.app_context_processor
def auth_context():
    login_form = LoginForm()

    context = {
        'header_form': login_form
    }

    return context


def load_user(user_id):
    return User.query.get(user_id)


def unauthorized_handler():
    flash('Ви маєте зайти в аккаунт, щоб перейти на наступну сторінку!',
          'danger',
          )

    next_url = url_for(request.endpoint, **request.view_args)
    return redirect(url_for('auth.login', next=next_url))
