from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

from app.utils.form_validators import NotExistModel
from app.models import User


class LoginForm(FlaskForm):

    name = StringField('Логін', validators=[
        DataRequired(),
        Length(max=50, message="Ім'я користувача має бути не більше 50 символів!"),
    ])
    password = PasswordField('Пароль', validators=[
        DataRequired(),
    ])
    is_remember = BooleanField("Запам'ятайте мене")
    recaptcha = RecaptchaField()
    submit = SubmitField('Вхід')


class RegistrationForm(FlaskForm):
    name = StringField('Логін', validators=[
        DataRequired(),
        Length(max=50, message="Ім'я користувача має бути не більше 50 символів!"),
        NotExistModel(User, 'name', "Користувач з таким ім'ям вже існує!"),
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email("Некоректний поштовий адрес!"),
        NotExistModel(User, 'email', "Користувач з таким поштовим адресом вже існує!"),
    ])
    password = PasswordField('Пароль', validators=[
        DataRequired(),
    ])
    password2 = PasswordField('Повторіть пароль', validators=[
        DataRequired(),
        EqualTo('password', 'Паролі не співпадають!'),
    ])
    recaptcha = RecaptchaField()
    submit = SubmitField('Реєстрація')
