from datetime import datetime

from app import db


class Project(db.Model):
    __tablename__ = "projects"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    title = db.Column(
        db.String(150),
        nullable=False
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    technologies = db.Column(
        db.String(500),
        nullable=True
    )

    github_url = db.Column(
        db.String(300),
        nullable=True
    )

    live_url = db.Column(
        db.String(300),
        nullable=True
    )

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

    updated_at = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False
    )

    user = db.relationship(
        "User",
        backref=db.backref(
            "projects",
            lazy=True
        )
    )

    def __repr__(self):
        return f"<Project {self.title}>"