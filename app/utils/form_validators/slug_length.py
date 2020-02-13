from wtforms.validators import ValidationError
from slugify import slugify


class SlugLength:
    def __init__(self, min=-1, max=-1, message=None):
        self.min = min
        self.max = max
        self.message = message or f"Your slug can't be between {min} and {max} " \
                                  f"characters long."

    def __call__(self, form, field):
        slug_len = len(slugify(field.data))
        if slug_len < self.min or self.max != -1 and slug_len > self.max:
            raise ValidationError(self.message)
