from flask import Blueprint, render_template


posts = Blueprint('posts_bp', __name__, template_folder='templates/posts',
                  static_folder='static')

from app.posts import routes
