from werkzeug.security import generate_password_hash, check_password_hash
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.Integer, db.ForeignKey('roles.id'))

    def __init__(self, username, email, password, role):
        self.username = username
        self.email = email
        self.role = role
        self.set_password(password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(32), unique = True)
    users = db.relationship('User', backref = 'usrs')

    def __init__(self, rolename):
        self.role_name = rolename

    def __repr__(self):
        return 'Role: {}'.format(self.role_name)


