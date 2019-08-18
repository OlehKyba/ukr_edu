from flask import Markup, url_for


class Message:

    def __init__(self, message=''):
        self.message = Markup(message)

    def result(self):
        return self.message

    def link(self, text, href, class_name='alert-link'):
        link_str = f'<a class="{class_name}" href="{url_for(href)}">{text}</a>'
        self.message += Markup(link_str)
        return self

    def text(self, text):
        self.message += Markup(text)
        return self

    def strong(self, text):
        self.message += Markup(f'<strong>{text}</strong>')
        return self
