from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


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
