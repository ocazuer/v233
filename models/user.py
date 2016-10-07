from . import ModelMixin
from . import db
from . import timestamp


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    # 明文储存密码
    password = db.Column(db.String())
    avatar = db.Column(db.String())
    # relationship
    comments = db.relationship('Comment', backref="user")

    def __init__(self, form):
        self.username = form.get('username', '')
        self.password = form.get('password', '')
        self.avatar = form.get('avatar', '')


    def validate_register(self):
        return len(self.username) > 2 and (User.query.filter_by(username=self.username).first() is None)

    def validate_login(self, u):
        return u.username == self.username and u.password == self.password