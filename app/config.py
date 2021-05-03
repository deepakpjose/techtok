"""
Settings for the flask app is set here.
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Base class for all the configs
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOADED_GIFS_DEST = os.getcwd() + '/docs'
    POSTS_PER_PAGE = 9

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')
