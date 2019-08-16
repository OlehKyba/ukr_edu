from .extentions import db
from datetime import datetime


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


class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=True)

    posts = db.relationship('Post',
                            foreign_keys='Post.author_id',
                            backref='author')

    roles = db.relationship('Role', secondary=roles, lazy='subquery',
                            backref=db.backref('users'))


class Role(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    subtitle = db.Column(db.String(240), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    date = db.Column(db.DateTime, default=datetime.now())
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('posts', lazy=True))


class Tag(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(100), nullable=False, unique=True)
