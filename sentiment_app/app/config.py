import os

class Development:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev_secret_key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
