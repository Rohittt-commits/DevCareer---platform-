from datetime import datetime

from app import db


class JobApplication(db.Model):
    __tablename__ = "job_applications"

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id"),
        nullable=False
    )

    company = db.Column(
        db.String(150),
        nullable=False
    )

    position = db.Column(
        db.String(150),
        nullable=False
    )

    job_url = db.Column(
        db.String(500),
        nullable=True
    )

    location = db.Column(
        db.String(150),
        nullable=True
    )

    status = db.Column(
        db.String(50),
        nullable=False,
        default="Wishlist"
    )

    applied_date = db.Column(
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
            "job_applications",
            lazy=True
        )
    )

    def __repr__(self):
        return f"<JobApplication {self.company} - {self.position}>"