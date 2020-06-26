import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '32UHRE34932420F'