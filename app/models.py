from .extentions import db


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


class Post(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    subtitle = db.Column(db.String(240), nullable=False)
    text = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(100), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    tags = db.relationship('Tag', secondary=tags, lazy='subquery',
                           backref=db.backref('posts', lazy=True))


class Tag(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(100), nullable=False, unique=True)
