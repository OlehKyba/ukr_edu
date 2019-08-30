from flask import render_template, flash, redirect, url_for, request

from .forms import PostForm

from app.models import Post, Tag, get_or_create
from app.extentions import db

from sqlalchemy.orm import subqueryload
from collections import namedtuple
from functools import wraps


def post_action(strategy_factory):

    @wraps(strategy_factory)
    def action(slug):
        strategy = strategy_factory()
        post = strategy.post_factory(slug)
        post_form = PostForm(obj=post)

        if request.method == 'GET':
            tags = [tag.value for tag in post.tags]
            post_form.tags.data = ','.join(tags)

        if post_form.validate_on_submit() and request.method == 'POST':
            values = post_form.tags.data.split(',')
            post_form.tags.data = [get_or_create(Tag, value=value)
                                   for value in values]

            post_form.populate_obj(post)
            db.session.add(post)
            db.session.commit()

            flash(*strategy.message)
            return redirect(strategy.next_page(post))

        return render_template('create-post.html',
                               post_form=post_form,
                               title=strategy.title,
                               )

    return action


PostStrategy = namedtuple('PostStrategy',
                          ['post_factory',
                           'next_page',
                           'message',
                           'title',
                           ])


@post_action
def create_post():

    create_strategy = PostStrategy(
        post_factory=lambda slug: Post(),
        next_page=lambda post: url_for('posts_bp.post', slug=post.slug),
        message=('Створенно новий пост!', 'success'),
        title='Новий пост'
    )
    return create_strategy


@post_action
def update_post():

    update_strategy = PostStrategy(
        post_factory=lambda slug: Post.query.filter_by(
            slug=slug).first_or_404(),
        next_page=lambda post: url_for('posts_bp.post', slug=post.slug),
        message=('Змінено цей пост!', 'primary'),
        title='Редагування'
    )

    return update_strategy
