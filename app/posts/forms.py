from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField, BooleanField, FileField, SubmitField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectMultipleField

from app.markup_messages import Message
from app.models import Tag


class PostForm(FlaskForm):

    title = StringField('Заголовок', validators=[
                        DataRequired(), Length(max=120)])
    subtitle = StringField('Підзаголовок', validators=[
                           DataRequired(), Length(max=240)])
    text = TextAreaField('Оснонвний текст статті', validators=[DataRequired()])
    tags = QuerySelectMultipleField(
        'Введіть теги:', query_factory=lambda: Tag.query, get_pk=lambda tag: tag.value, allow_blank=True,)
    image = FileField(Message().span('Виберіть файл', id='fileName').result())
    date = DateField('Дата публікації:')
    submit = SubmitField('OK')
