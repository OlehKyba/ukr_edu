from flask import render_template, flash, redirect, url_for, request

from .forms import PostForm

from app.models import Post, Tag
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
        post_form.tags.query = Tag.query.options(
            subqueryload(Tag.posts)).filter(Post.id == post.id)

        if post_form.validate_on_submit()
        and request.method == strategy.method:

            post_form.populate_obj(post)
            # TODO: Normal tag saving.
            db.session.add(post)
            db.session.commit()

            flash(*strategy.message)
            return redirect(strategy.next_page(post))

        return render_template('create-post.html', post_form=post_form,
                               method=strategy.method)

    return action


PostStrategy = namedtuple('PostStrategy',
                          ['post_factory',
                           'method',
                           'next_page',
                           'message'])


@post_action
def create_post():

    create_strategy = PostStrategy(
        post_factory=lambda slug: Post(),
        next_page=lambda post: url_for('posts_bp.post', slug=post.slug),
        message=('Створенно новий пост!', 'success'),
        method='POST',
    )
    return create_strategy


@post_action
def update_post():

    update_strategy = PostStrategy(
        post_factory=lambda slug: Post.query.filter_by(
            slug=slug).first_or_404(),
        next_page=lambda post: url_for('posts_bp.post', slug=post.slug),
        message=('Змінено цей пост!', 'primary'),
        method='POST',
    )

    return update_strategy
