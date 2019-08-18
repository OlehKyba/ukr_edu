from flask import render_template, redirect, flash, url_for, Markup
from flask.views import MethodView
from flask_login import current_user, login_user

from .forms import LoginForm

from app.models import User
from app.markup_messages import Message


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
                    'Забули пароль?', 'index').result()

                flash(invalid_message, category='danger')

                return redirect(url_for('index'))
            login_user(user, remember=form.is_remember.data)

            success_message = Message('Ви зайшли на акаунт ').strong(
                current_user.name).text('!').result()

            flash(success_message, 'success')

        return redirect(url_for('index'))
