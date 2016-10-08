from . import ModelMixin
from . import db
from . import timestamp

import hashlib


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
        self.avatar = self.random_avatar()


    def validate_register(self):
        return len(self.username) > 2 and (User.query.filter_by(username=self.username).first() is None)

    def validate_login(self, u):
        return u.username == self.username and u.password == self.password

    def random_avatar(self):
        # code from here: https://zh-tw.gravatar.com/site/implement/images/python/

        username = self.username.encode('utf-8')
        # email = "someone@somewhere2.com".encode('utf-8')
        default = "retro"
        size = 40
        gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(username.lower()).hexdigest() + "?"
        gravatar_url += 's={}&d={}'.format(size, default)
        return gravatar_url