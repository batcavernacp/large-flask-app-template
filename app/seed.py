from app.models.post import Post
from app.extensions import db

def seed():
    new_post = Post(content = "content", title = "title")
    db.session.add(new_post)
    db.session.commit()