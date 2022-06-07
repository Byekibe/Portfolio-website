from os import environ, path
from dotenv import load_dotenv

class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False