from flask import Flask
from flask_wtf import CSRFProtect
from .models import db

def create_app():
    app = Flask(__name__)

    # Required for CSRF + sessions
    app.config["SECRET_KEY"] = "change-me-in-prod"

    # SQLite DB (instance/app.db)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Init extensions
    db.init_app(app)
    CSRFProtect(app)

    # Create tables
    with app.app_context():
        db.create_all()

    # Register routes
    from .routes import main as main_bp
    app.register_blueprint(main_bp)

    return app
