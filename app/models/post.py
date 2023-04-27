from app.models import Model
from app.extensions.database import db
from dataclasses import dataclass
from marshmallow import fields, Schema

@dataclass
class Post(Model):
    title: str = db.Column(db.String(150))
    content: str = db.Column(db.Text)

class PostSchema(Schema):
    title = fields.String(required=True)
    content = fields.String(required=True)