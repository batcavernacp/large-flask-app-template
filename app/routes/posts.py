from app.routes import posts_bp as bp
from app.services.posts import getAllPosts

@bp.route('/')
def index():
    return getAllPosts()
