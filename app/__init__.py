import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from dotenv import load_dotenv


load_dotenv()


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    # =========================
    # APPLICATION CONFIGURATION
    # =========================

    app.config["SECRET_KEY"] = os.getenv(
        "SECRET_KEY",
        "devcareer-development-key"
    )

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devcareer.db"

    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # =========================
    # INITIALIZE EXTENSIONS
    # =========================

    db.init_app(app)
    login_manager.init_app(app)

    # =========================
    # FLASK-LOGIN CONFIGURATION
    # =========================

    login_manager.login_view = "auth.login"

    # =========================
    # IMPORT MODELS
    # =========================

    from app.models.user import User
    from app.models.project import Project
    from app.models.skill import Skill
    from app.models.application import JobApplication
    from app.models.goal import Goal
    from app.models.learning import Learning

    # =========================
    # FLASK-LOGIN USER LOADER
    # =========================

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # =========================
    # REGISTER BLUEPRINTS
    # =========================

    from app.routes.main import main
    app.register_blueprint(main)

    from app.routes.auth import auth
    app.register_blueprint(auth)

    from app.routes.projects import projects
    app.register_blueprint(projects)

    from app.routes.skills import skills
    app.register_blueprint(skills)

    from app.routes.applications import applications
    app.register_blueprint(applications)

    from app.routes.goals import goals
    app.register_blueprint(goals)

    from app.routes.learning import learning
    app.register_blueprint(learning)

    from app.routes.api import api
    app.register_blueprint(api)

    return app