from flask import render_template

from . import posts
from .views import create_post, update_post

from app.models import Post


posts.add_url_rule('/edit/', defaults={'slug': None},
                   view_func=create_post, methods=['GET', 'POST'])

posts.add_url_rule('/edit/<slug>',
                   view_func=update_post, methods=['GET', 'POST'])


@posts.route('/<slug>')
def post(slug):
    post = Post.query.filter_by(slug=slug).first_or_404()
    new_posts = Post.query.filter(
        id != post.id).order_by(Post.date.desc()).limit(3)
    return render_template('post.html', post=post, new_posts=new_posts)
