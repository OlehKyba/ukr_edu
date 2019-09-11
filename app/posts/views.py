from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user

from .forms import PostForm

from app.models import Post, Tag, get_or_create
from app.extentions import db

from sqlalchemy.orm import subqueryload
from collections import namedtuple
from functools import wraps, partial


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

        if post_form.validate_on_submit():
            post_form.tags.data = TagInputAdapter.data_to_taglist(
                post_form.tags.data)

            post_form.populate_obj(post)

            if not post.author:
                post.author = current_user

            db.session.add(post)
            db.session.commit()

            flash(*strategy.message)
            return redirect(strategy.next_page(post))

        post_form.tags.data = TagInputAdapter.taglist_to_data(post.tags)
        return render_template('create-post.html',
                               post_form=post_form,
                               title=strategy.title,
                               )

    return action


def paginate(template, per_page=1):
    def paginate_init(context_factory):
        @wraps(context_factory)
        def paginate_wraper(slug, page):
            context = context_factory(slug, page)
            base_query_obj = context['pages']
            context['pages'] = base_query_obj.paginate(
                page=page, per_page=per_page)
            return render_template(template, **context)
        return paginate_wraper
    return paginate_init


PostStrategy = namedtuple('PostStrategy',
                          ['post_factory',
                           'next_page',
                           'message',
                           'title',
                           ])
