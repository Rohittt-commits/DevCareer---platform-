from datetime import datetime

from app import db


class Learning(db.Model):
    __tablename__ = "learning"

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

    category = db.Column(
        db.String(100),
        nullable=True
    )

    description = db.Column(
        db.Text,
        nullable=True
    )

    resource_url = db.Column(
        db.String(500),
        nullable=True
    )

    progress = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    status = db.Column(
        db.String(50),
        nullable=False,
        default="Not Started"
    )

    start_date = db.Column(
        db.Date,
        nullable=True
    )

    completion_date = db.Column(
        db.Date,
        nullable=True
    )

    notes = db.Column(
        db.Text,
        nullable=True
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
            "learning_items",
            lazy=True
        )
    )

    def __repr__(self):
        return f"<Learning {self.title}>"