from app.models import Model
from app.extensions import db
from dataclasses import dataclass

@dataclass
class Question(Model):
    content: str = db.Column(db.Text)
    answer: str = db.Column(db.Text)
