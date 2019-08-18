from flask import redirect, flash, url_for
from flask_login import current_user, login_user, logout_user

from . import auth
from .views import LoginView

from app.models import User
from app.markup_messages import Message


auth.add_url_rule(
    '/login', view_func=LoginView.as_view('login'), methods=['GET', 'POST'])


@auth.route('/logout')
def logout():
    logout_message = Message('Ви вийшли з акаунта ').strong(
        current_user.name).text('!').result()

    flash(logout_message, 'primary')
    logout_user()
    return redirect(url_for('index'))
