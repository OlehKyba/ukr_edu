from flask import Blueprint, render_template
from .forms import PostForm
from app.models import Post, Tag
from sqlalchemy.orm import subqueryload


posts = Blueprint('posts_bp', __name__, template_folder='templates/posts',
                  static_folder='static')


"""
@posts.route('/create')
def create():
    obj = Post()
    post_form = PostForm(obj=obj)
    post_form.tags.query = Tag.query.options(subqueryload(Tag.posts)).filter(Post.id == obj.id)
    return render_template('create-post.html', post_form=post_form)
"""
