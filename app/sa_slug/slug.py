from flask_sqlalchemy import Model
import sqlalchemy as sa
from slugify import slugify
from functools import wraps


def _memoized(func):
    cls_dict = {}

    @wraps(func)
    def cashe(column, length):
        clsname = f'Slug{column.capitalize()}{str(length)}'
        cls = cls_dict.get(clsname)

        if cls:
            return cls

        cls = func(column, length, clsname)
        cls_dict[clsname] = cls
        return cls
    return cashe


def _set_factory(column):

    def setter(self, name, value):

        if name == column:
            super(Model, self).__setattr__('slug', slugify(value))
            # set_attribute(self, 'slug', slugify(value))

        super(Model, self).__setattr__(name, value)
        # set_attribute(self, name, value)

    return setter


@_memoized
def SlugMixin(column: str, length, clsname=None):
    slug = type(f'Slug{column.capitalize()}{str(length)}', (Model, ), {
        'slug': sa.Column(sa.String(length), unique=True),
        '__setattr__': _set_factory(column),
    })
    return slug
