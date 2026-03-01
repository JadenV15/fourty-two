from flask import Flask
import os
from pathlib import Path

from . import fourtytwo
from . import db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=str(Path(app.instance_path).resolve() / 'digits')
    )

    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    Path(app.instance_path).mkdir(parents=True, exist_ok=True)
    
    db.init_app(app)
    app.register_blueprint(fourtytwo.bp)
    
    return app
    
if __name__ == '__main__':
    pass