from app.extensions import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Model(db.Model):
    __abstract__ = True
    
    id: int = db.Column(db.Integer, primary_key=True)
    created_at: datetime = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at: datetime = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    deleted: bool = db.Column(db.Boolean, default=False)

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def serialize(self):
        """Serialize the model to a dictionary."""
        serialized_data = {}
        for column in self.__table__.columns:
            if isinstance(getattr(self, column.name), datetime):
                serialized_data[column.name] = str(getattr(self, column.name))
            else:
                serialized_data[column.name] = getattr(self, column.name)
        return serialized_data