from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, FileField, SubmitField
from flask_wtf.file import FileAllowed

from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length

from datetime import datetime

from app.utils.markup_messages import Message


class PostForm(FlaskForm):
    submit = SubmitField('OK')
    tags = StringField('Введіть теги:', default='')
    date = DateField('Дата публікації:', default=datetime.now())
    image = FileField(Message().span('Виберіть файл', id='fileName').result(
    ), validators=[FileAllowed([
        'jpg',
        'png',
        'svg',
    ],
        'До статті можна прикріпити лише зображення!',
    )])

    title = StringField('Заголовок', validators=[
        DataRequired(),
        Length(max=120),
    ])

    subtitle = StringField('Підзаголовок', validators=[
        DataRequired(),
        Length(max=120),
    ])

    text = TextAreaField('Оснонвний текст статті', validators=[
            DataRequired(),
    ])
