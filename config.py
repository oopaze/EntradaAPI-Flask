import os
from datetime import timedelta

from decouple import config


class Config(object):
    JWT_AUTH_USERNAME_KEY = 'username'
    JWT_EXPIRATION_DELTA = timedelta(days=30)
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=30)
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=30)
    JWT_AUTH_URL_RULE = '/login'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = config("SECRET_KEY", default="dasdadsadsaa")
    


class Development(Config):
    ENV = 'development'
    DEBUG = True
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'biblioteca.db')
    if config("SQLALCHEMY_DATABASE_URI", default=None):
        SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')     


class Production(Config):
    ENV = 'production'
    DEBUG = False
    basedir = os.path.abspath(os.path.dirname(__file__))

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'biblioteca.db')
    if config("SQLALCHEMY_DATABASE_URI", default=None):
        SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')     

    
