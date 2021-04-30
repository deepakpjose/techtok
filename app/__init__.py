from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect

def create_app():
    app = Flask(__name__)

    bootstrap = Bootstrap(app)
    csrf = CSRFProtect(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
