from app.models import Model
from app.extensions import db
from dataclasses import dataclass

@dataclass
class Post(Model):
    title: str = db.Column(db.String(150))
    content: str = db.Column(db.Text)
