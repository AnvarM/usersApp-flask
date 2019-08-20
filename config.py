import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or "Seeeecret key"
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://user:password@localhost/db'
    SQLALCHEMY_POOL_RECYCLE =86400
    SQLALCHEMY_TRACK_MODIFICATIONS = False

