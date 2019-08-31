from flask import render_template, flash, redirect, url_for, request

from .forms import PostForm

from app.models import Post, Tag, get_or_create
from app.extentions import db

from sqlalchemy.orm import subqueryload
from collections import namedtuple
from functools import wraps


class TagInputAdapter:

    @staticmethod
    def taglist_to_data(taglist: list) -> str:
        values = [tag.value for tag in taglist]
        return ','.join(values)

    @staticmethod
    def data_to_taglist(data: str) -> list:
        values = data.split(',')
        taglist = [get_or_create(Tag, value=value) for value in values]
        return taglist


def post_action(strategy_factory):

    @wraps(strategy_factory)
    def action(slug):
        strategy = strategy_factory()
        post = strategy.post_factory(slug)
        post_form = PostForm(obj=post)

        if request.method == 'GET':
            post_form.tags.data = TagInputAdapter.taglist_to_data(post.tags)

        if post_form.validate_on_submit() and request.method == 'POST':
            post_form.tags.data = TagInputAdapter.data_to_taglist(
                post_form.tags.data)

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
