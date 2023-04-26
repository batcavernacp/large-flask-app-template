from app.models import Model
from app.extensions import db

class Question(Model):
    content = db.Column(db.Text)
    answer = db.Column(db.Text)
