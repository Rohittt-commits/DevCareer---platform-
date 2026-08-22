from datetime import datetime

from app import db


class Goal(db.Model):
    __tablename__ = "goals"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

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

    category = db.Column(
        db.String(100),
        nullable=True
    )

    target_date = db.Column(
        db.Date,
        nullable=True
    )

    status = db.Column(
        db.String(50),
        nullable=False,
        default="Not Started"
    )

    progress = db.Column(
        db.Integer,
        nullable=False,
        default=0
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
            "goals",
            lazy=True
        )
    )

    def __repr__(self):
        return f"<Goal {self.title}>"