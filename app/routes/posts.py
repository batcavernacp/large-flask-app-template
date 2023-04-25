from flask import render_template
from app.routes import posts_bp as bp
from app.extensions import db
from app.models.post import Post

@bp.route('/')
def index():
    posts = Post.query.all()
    return posts
