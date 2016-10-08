from . import ModelMixin
from . import db
from . import timestamp


class Topic(db.Model, ModelMixin):
    __tablename__ = 'topics'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    content = db.Column(db.String())
    # has relationship with node
    node_id = db.Column(db.Integer, db.ForeignKey('nodes.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref="topic")

    def __init__(self, form):
        self.title = form.get('title', '')
        self.content = form.get('content', '')
        self.node_id = form.get('node_id', '')
        self.user_id = form.get('user_id', '')
