from app.extensions import db
from app.utils.encoder import AlchemyEncoder
import json
from datetime import datetime


class Model(db.Model):
    __abstract__ = True
    id = db.Column(db.Integer, primary_key=True)
    createdAt = db.Column(db.DateTime, default=datetime.utcnow)
    updatedAt = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted = db.Column(db.Boolean, default=False)

    def serialize(self):
        return json.dumps(self, cls=AlchemyEncoder)