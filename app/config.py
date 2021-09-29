"""
Settings for the flask app is set here.
"""
import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """
    Base class for all the configs
    """

    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    UPLOAD_FOLDER = os.getenv("APP_PATH") + "/docs"
    ALLOWED_EXTENSIONS = {
        "txt",
        "pdf",
        "png",
        "jpg",
        "jpeg",
        "gif",
        "webp",
        "docx",
        "doc",
    }

    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "data.sqlite")
