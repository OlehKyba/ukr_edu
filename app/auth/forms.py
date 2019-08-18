from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):

    name = StringField('Логін', validators=[DataRequired(), Length(max=50)])
    password = PasswordField('Пароль', validators=[DataRequired()])
    is_remember = BooleanField("Запам'ятайте мене")
    submit = SubmitField('Вхід')
