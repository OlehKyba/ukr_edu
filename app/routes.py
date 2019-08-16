from flask import current_app, render_template
from .models import Post


@current_app.route("/")
def index():
    posts = Post.query.order_by(Post.date.desc()).limit(3)
    for i in posts:
        print(i.title, i.date)
    return render_template('index.html', current_user=False, posts=posts)
