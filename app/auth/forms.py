from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):

    username = StringField('Логін', validators=DataRequired())
    password = PasswordField('Пароль', validators=DataRequired())
    is_remember = BooleanField("Запам'ятайте мене")
    submit = SubmitField('Вхід ')
