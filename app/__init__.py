from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # Application configuration
    app.config["SECRET_KEY"] = "devcareer-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devcareer.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)

    # Flask-Login configuration
    login_manager.login_view = "auth.login"

    # Import User model
    from app.models.user import User

    # Flask-Login user loader
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # Register Main blueprint
    from app.routes.main import main
    app.register_blueprint(main)

    # Register Authentication blueprint
    from app.routes.auth import auth
    app.register_blueprint(auth)

    # Register Projects blueprint
    from app.routes.projects import projects
    app.register_blueprint(projects)

    return app