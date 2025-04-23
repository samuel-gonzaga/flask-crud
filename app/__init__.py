from flask import Flask
from .models import db
from .routes import main_bp
from .config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.register_blueprint(main_bp)

    return app
