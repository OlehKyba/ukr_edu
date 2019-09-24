from flask_wtf import FlaskForm

from wtforms import (StringField,
                     TextAreaField,
                     BooleanField,
                     FileField,
                     SelectMultipleField,
                     SubmitField)
from flask_wtf.file import FileAllowed

from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.orm import model_form

from datetime import datetime

from app.markup_messages import Message
from app.models import Post
from app.extentions import db


class _SubmitTagDateMixin(FlaskForm):
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


settings = {
    'title': {
        'label': 'Заголовок',
        'validators': [
            DataRequired(),
            Length(max=120),
        ],
    },

    'subtitle': {
        'label': 'Підзаголовок',
        'validators': [
            DataRequired(),
            Length(max=240),
        ],
    },

    'text': {
        'label': 'Оснонвний текст статті',
        'validators': [
            DataRequired(),
        ],
    },
}

PostForm = model_form(Post,
                      db_session=db.session,
                      base_class=_SubmitTagDateMixin,
                      field_args=settings,
                      exclude=[
                          'tags',
                          'date',
                          '_image',
                      ],
                      )
