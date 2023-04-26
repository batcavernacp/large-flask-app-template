from app.models import Model
from app.extensions import db

class Post(Model):
    title = db.Column(db.String(150))
    content = db.Column(db.Text)
