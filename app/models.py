from .extentions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from app.settings import S3_IMG_BUCKET
from app.sa_slug import SlugMixin
from app.descriptors.files import FileDescriptor
from app.descriptors.files.strategies import S3Strategy


roles = db.Table('roles',
                 db.Column('user_id', db.Integer, db.ForeignKey('user.id'),
                           primary_key=True),
                 db.Column('role_id', db.Integer, db.ForeignKey('role.id'),
                           primary_key=True)
                 )

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'),
                          primary_key=True),
                db.Column('post_id', db.Integer, db.ForeignKey('post.id'),
                          primary_key=True)
                )


class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)

    posts = db.relationship('Post',
                            foreign_keys='Post.author_id',
                            backref=db.backref('author', lazy='subquery'))

    roles = db.relationship('Role', secondary=roles, lazy='subquery',
                            backref=db.backref('users'))

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def is_correct_password(self, password):
        return check_password_hash(self.password, password)

    def is_author(self, post):
        return post.author.id == self.id


class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Post(db.Model, SlugMixin('title', 120)):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    subtitle = db.Column(db.String(240), nullable=False)
    text = db.Column(db.Text, nullable=False)
    _image = db.Column('image', db.String(100), nullable=True)
    image = FileDescriptor(S3Strategy(S3_IMG_BUCKET), name_from='slug')
    date = db.Column(db.DateTime, default=datetime.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('posts', lazy='dynamic'))


class Tag(db.Model, SlugMixin('value', 100)):

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(100), nullable=False, unique=True)


def get_or_create(model, session=db.session, **kwargs):
    # If a new entity is created, it needs db.session.commit().
    exists_model = session.query(model).filter_by(**kwargs).first()
    return exists_model or model(**kwargs)
