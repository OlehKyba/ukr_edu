from wtforms.validators import ValidationError


class NotExistModel:

    def __init__(self, model, field, message=None):
        self.model = model
        self.field_name = field
        self.message = message or f'Entity with this {self.field_name} already exist!'

    def __call__(self, form, field):
        data = field.data
        kwargs = {self.field_name: data}
        obj = self.model.query.filter_by(**kwargs).first()
        if obj:
            raise ValidationError(self.message)
