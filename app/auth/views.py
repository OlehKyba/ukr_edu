from flask import render_template, redirect, flash, url_for, request
from flask.views import MethodView
from flask_login import current_user, login_user

from .forms import LoginForm

from app.models import User
from app.utils.markup_messages import Message
from app.utils import redirect_or_default


class LoginView(MethodView):

    def get(self):
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        return render_template('login.html',
                               login_form=LoginForm())

    def post(self):
        form = LoginForm()

        if current_user.is_authenticated:
            return redirect(url_for('index'))

        if form.validate_on_submit():
            user = User.query.filter_by(name=form.name.data).first()

            if not user or not user.is_correct_password(form.password.data):
                invalid_message = Message(
                    'Некоректні логін або пароль! ').link(
                    'Забули пароль?',
                    href='index',
                    class_='alert-link'
                    ).result()

                flash(invalid_message, category='danger')

                return redirect(url_for('auth.login'))

            login_user(user, remember=form.is_remember.data)

            success_message = Message('Ви зайшли на акаунт ').strong(
                current_user.name).text('!').result()

            flash(success_message, 'success')

        possibly_next = request.args.get('next')
        default = url_for('index')
        return redirect_or_default(possibly_next, default)
