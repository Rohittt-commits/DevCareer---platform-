from datetime import datetime

from app import db


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)

    tech_stack = db.Column(db.String(300), nullable=False)

    github_url = db.Column(db.String(300), nullable=True)
    live_url = db.Column(db.String(300), nullable=True)

    status = db.Column(
        db.String(50),
        nullable=False,
        default="In Progress"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )