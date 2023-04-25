from app.routes import posts_bp as bp
from app.models.post import Post

@bp.route('/')
def index():
    posts = Post.query.all()
    return posts
