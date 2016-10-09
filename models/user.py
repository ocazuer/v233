from . import ModelMixin
from . import db
from . import timestamp

import hashlib

def hash_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()


class User(db.Model, ModelMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(), unique=True)
    # md5 密文储存密码
    password = db.Column(db.String())
    avatar = db.Column(db.String())
    created_time = db.Column(db.Integer)
    updated_time = db.Column(db.Integer)
    # relationship
    comments = db.relationship('Comment', backref="user")
    topics = db.relationship('Topic', backref="user")

    def __init__(self, form):
        self.created_time = timestamp()
        self.username = form.get('username', '')
        self.password = hash_md5(form.get('password', ''))
        self.avatar = self.random_avatar()


    def validate_register(self):
        c1 = len(self.username) >= 2
        c2 = len(self.username) <= 20
        c3 = User.query.filter_by(username=self.username).first() is None
        return c1 and c2 and c3

    def validate_login(self, u):
        return u.username == self.username and u.password == self.password

    def random_avatar(self):
        # code from here: https://zh-tw.gravatar.com/site/implement/images/python/

        username = self.username.encode('utf-8')
        # email = "someone@somewhere2.com".encode('utf-8')
        default = "retro"
        size = 80
        gravatar_url = "https://www.gravatar.com/avatar/" + hashlib.md5(username.lower()).hexdigest() + "?"
        gravatar_url += 's={}&d={}'.format(size, default)
        return gravatar_url