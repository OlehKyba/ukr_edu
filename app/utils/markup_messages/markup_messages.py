from flask import Markup, url_for


class Message:

    def __init__(self, message=''):
        self.message = Markup(message)

    def result(self):
        return self.message

    def link(self, text, **kwargs):
        link_str = f'<a {self._attr_render(**kwargs)}>{text}</a>'
        self.message += Markup(link_str)
        return self

    def text(self, text):
        self.message += Markup(text)
        return self

    def strong(self, text, **kwargs):
        self.message += Markup(
            f'<strong {self._attr_render(**kwargs)}>{text}</strong>')
        return self

    def span(self, text, **kwargs):
        self.message += Markup(
            f'<span {self._attr_render(**kwargs)}>{text}</span>')
        return self

    @staticmethod
    def _attr_render(**kwargs):
        args = map(lambda item: (Message._attr_filter(
            item[0]), item[1]), kwargs.items())
        return ' '.join([f'{key}={value}' for key, value in args])

    @staticmethod
    def _attr_filter(item):
        change = {
            'class_': 'class'
        }

        return change.get(item, item)
