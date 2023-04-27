from app.models import Model, Schema
from app.extensions.database import db
from dataclasses import dataclass
from marshmallow import fields

@dataclass
class Question(Model):
    content: str = db.Column(db.Text)
    answer: str = db.Column(db.Text)

class QuestionSchema(Schema):
    title = fields.String(required=True)
    answer = fields.Integer(required=True)