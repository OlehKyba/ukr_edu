from werkzeug.urls import url_parse
from flask import request, redirect, url_for


def redirect_or_default(possibly_next, default):
    next_page = default
    if possibly_next and url_parse(possibly_next).netloc == '':
        next_page = possibly_next

    return redirect(next_page)
