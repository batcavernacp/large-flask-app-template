from app.routes import posts_bp as bp
from app.services.posts import getAllPosts, createPost
from flask import request, json

@bp.get('/')
def list():
    return getAllPosts()

@bp.post('/')
def create():
    data = json.loads(request.data)

    new_post = createPost(data)

    return new_post.serialize()

