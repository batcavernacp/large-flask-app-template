from app.models.post import Post
from app.extensions.database import db

def get_posts():
    return Post.query.all()

def create_post(request):
    content = request['content']
    title = request['title']
    new_post = Post(content=content, title=title)
    db.session.add(new_post)
    db.session.commit()

    return new_post

def edit_post(id, request):
    post = Post.query.get(id)
    post.title = request['title']
    post.content = request['content']
    db.session.commit()
    return post

def delete_post(id):
    post = Post.query.get(id)
    post.deleted = True
    db.session.commit()
    return post

def get_post(id):
    return Post.query.get(id)