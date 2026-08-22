from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "devcareer-secret-key"
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///devcareer.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)
    login_manager.init_app(app)

    login_manager.login_view = "auth.login"

    from app.models.user import User
    from app.models.project import Project
    from app.models.skill import Skill
    from app.models.application import JobApplication
    from app.models.goal import Goal

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

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

    return app