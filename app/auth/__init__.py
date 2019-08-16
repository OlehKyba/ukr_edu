from flask import Blueprint, render_template
from .forms import LoginForm


auth = Blueprint('auth', __name__)


@auth.app_context_processor
def auth_context():
    header_form = LoginForm()

    context = {
        'header_form': header_form
    }

    return context
