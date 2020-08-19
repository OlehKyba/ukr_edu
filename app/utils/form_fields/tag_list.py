from wtforms import Field
from wtforms.widgets import TextInput


class TagListField(Field):
    widget = TextInput()

    def __init__(self, parser, label='', validators=None, **kwargs):
        super(TagListField, self).__init__(label, validators, **kwargs)
        self.parser = parser

    def _value(self):
        if self.data and self.data != '':
            return self.parser.stringify(self.data)
        return ''

    def process_formdata(self, value_list):
        self.data = self.parser.parse(value_list[0]) if value_list else []
