from flask_login import UserMixin

from blog.app import db


class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    name = db.Column(db.String(255))
    password = db.Column(db.String(255))
    is_staff = db.Column(db.Boolean, nullable=False, default=False)

    def __init__(self, email, password, name, is_staff):
        self.email = email
        self.name = name
        self.password = password
        self.is_staff = is_staff
