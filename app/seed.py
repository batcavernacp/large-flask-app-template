from app.models.post import Post
from app.models.question import Question
from app.extensions import db

def seed():
    new_post = Post(content = "content", title = "title")
    new_question = Question(content = "content", answer = "answer")
    db.session.add(new_question)
    db.session.add(new_post)
    db.session.commit()