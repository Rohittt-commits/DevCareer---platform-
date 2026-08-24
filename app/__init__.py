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

    # Import models
    from app.models.user import User
    from app.models.project import Project
    from app.models.skill import Skill
    from app.models.application import JobApplication
    from app.models.goal import Goal
    from app.models.learning import Learning

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

    # Register Skills blueprint
    from app.routes.skills import skills
    app.register_blueprint(skills)

    # Register Applications blueprint
    from app.routes.applications import applications
    app.register_blueprint(applications)

    # Register Goals blueprint
    from app.routes.goals import goals
    app.register_blueprint(goals)

    # Register Learning blueprint
    from app.routes.learning import learning
    app.register_blueprint(learning)

    return app