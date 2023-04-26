from app.models.post import Post
from app.extensions import db

def getAllPosts():
    return Post.query.all()

def createPost(form):
    # TODO: validar form
    content = form.get('content')
    title = form.get('title')

    new_post = Post(content=content, title=title)

    db.session.add(new_post)
    db.session.commit()

    return new_post