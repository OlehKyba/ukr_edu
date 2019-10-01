from werkzeug.urls import url_parse
from flask import redirect, flash, url_for, request
from flask_login import current_user, login_user, logout_user

from . import auth
from .views import LoginView

from app.models import User
from app.utils import redirect_or_default
from app.utils.markup_messages import Message


auth.add_url_rule(
    '/login', view_func=LoginView.as_view('login'), methods=['GET', 'POST'])


@auth.route('/logout')
def logout():
    logout_message = Message('Ви вийшли з акаунта ').strong(
        current_user.name).text('!').result()

    flash(logout_message, 'primary')
    logout_user()

    possibly_next = request.args.get('next')
    default = url_for('index')
    return redirect_or_default(possibly_next, default)
