from flask import render_template, flash, redirect
from flask_login import current_user

from .forms import PostForm
from .async_tasks import upload_post_preview

from app.extentions import db

from collections import namedtuple
from functools import wraps


def post_action(strategy_factory):

    @wraps(strategy_factory)
    def action(slug):
        strategy = strategy_factory()
        post = strategy.post_factory(slug)
        post_form = PostForm(obj=post)

        if post_form.validate_on_submit():

            image = post_form.image.data

            post.title = post_form.title.data
            post.date = post_form.date.data
            post.subtitle = post_form.subtitle.data
            post.text = post_form.text.data
            post.tags = post_form.tags.data

            if not post.author:
                post.author = current_user

            db.session.add(post)
            db.session.commit()

            if image:
                file_extension = image.filename.split('.')[-1]
                upload_post_preview.delay(post.id, image.stream, file_extension)

            flash(*strategy.success_message)
            return redirect(strategy.next_page(post))

        for error_field in post_form.errors:
            for error in post_form[error_field].errors:
                flash(error, 'danger')

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
                           'success_message',
                           'error_message',
                           'title',
                           ],
                          )
