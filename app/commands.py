import click
from flask.cli import with_appcontext

from .extentions import db
from .models import User, Role, Post, Tag


@click.command(name='create_tables')
@with_appcontext
def create_tables():
    db.create_all()
