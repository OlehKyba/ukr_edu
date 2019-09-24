from flask import render_template, url_for, flash, redirect

from . import posts
from .views import post_action, paginate, PostStrategy

from app.extentions import db
from app.models import Post, Tag
from app.markup_messages import Message


@posts.route('article/<slug>')
def post(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    new_posts = Post.query.filter(
        id != post.id).order_by(Post.date.desc()).limit(3)
    return render_template('post.html', post=post, new_posts=new_posts)


@posts.route('/edit/', defaults={'slug': None}, methods=['GET', 'POST'])
@post_action
def create_post():

    create_strategy = PostStrategy(
        post_factory=lambda slug: Post(),
        next_page=lambda post: url_for('posts_bp.post', slug=post.slug),
        success_message=('Створенно новий пост!', 'success'),
        error_message=lambda message: (message, 'danger'),
        title='Новий пост'
    )
    return create_strategy


@posts.route('/edit/<slug>', methods=['GET', 'POST'])
@post_action
def update_post():

    update_strategy = PostStrategy(
        post_factory=lambda slug: Post.query.filter_by(
            slug=slug).first_or_404(),
        next_page=lambda post: url_for('posts_bp.post', slug=post.slug),
        success_message=('Змінено цей пост!', 'primary'),
        error_message=lambda message: (message, 'danger'),
        title='Редагування'
    )

    return update_strategy


@posts.route('/delete/<slug>')
def delete_post(slug):
    post = Post.query.filter_by(
        slug=slug).first_or_404()

    db.session.delete(post)
    db.session.commit()

    message = Message('Видалений пост "').strong(
        post.title).text('" !').result()
    flash(message, 'danger')
    return redirect(url_for('posts_bp.all_posts'))


@posts.route('/', defaults={'slug': 'all', 'page': 1})
@posts.route('/<slug>', defaults={'page': 1})
@posts.route('/<slug>/<int:page>')
@paginate('paginate.html', 9)
def all_posts(slug, page):
    if page == 1:
        message = Message('Це статті для ').strong(
            'всіх').text(' відвідувачів!').result()
        flash(message, 'success')

    pages = Post.query.order_by(
        Post.date.desc())

    context = {
        'context': {
            'slug': slug,
        },
        'pages': pages,
        'link': 'posts_bp.all_posts',
    }

    return context


@posts.route('/tag/<slug>', defaults={'page': 1})
@posts.route('/tag/<slug>/<int:page>')
@paginate('paginate.html', 9)
def tag_posts(slug, page):

    tag = Tag.query.filter_by(slug=slug).first_or_404()

    if page == 1:
        message = Message('Це статті з тегом "').strong(
            tag.value).text('" !').result()
        flash(message, 'success')

    pages = tag.posts.order_by(
        Post.date.desc())

    context = {
        'context': {
            'slug': slug,
        },
        'pages': pages,
        'link': 'posts_bp.tag_posts',
    }

    return context
