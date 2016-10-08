from . import ModelMixin
from . import db
from . import timestamp


class Node(db.Model, ModelMixin):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    created_time = db.Column(db.Integer)
    updated_time = db.Column(db.Integer)
    # relationship
    topics = db.relationship('Topic', backref="node")

    def __init__(self, form):
        self.created_time = timestamp()
        self.name = form.get('name', '')
        self.description = form.get('description', '')
