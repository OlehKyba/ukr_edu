from flask import current_app, render_template
from .models import Post


@current_app.route("/")
@current_app.route("/index")
def index():
    posts = Post.query.order_by(Post.date.desc()).limit(3)
    return render_template('index.html', posts=posts)
