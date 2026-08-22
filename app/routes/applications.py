from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models.application import JobApplication


applications = Blueprint(
    "applications",
    __name__,
    url_prefix="/applications"
)


STATUSES = [
    "Wishlist",
    "Applied",
    "Assessment",
    "Interview",
    "Offer",
    "Rejected",
    "Withdrawn"
]


@applications.route("/")
@login_required
def list_applications():
    user_applications = JobApplication.query.filter_by(
        user_id=current_user.id
    ).order_by(
        JobApplication.created_at.desc()
    ).all()

    return render_template(
        "applications/list.html",
        applications=user_applications
    )


@applications.route("/add", methods=["GET", "POST"])
@login_required
def add_application():

    if request.method == "POST":

        company = request.form.get("company", "").strip()
        position = request.form.get("position", "").strip()
        job_url = request.form.get("job_url", "").strip()
        location = request.form.get("location", "").strip()
        status = request.form.get("status", "Wishlist")
        applied_date = request.form.get("applied_date")
        notes = request.form.get("notes", "").strip()

        if not company:
            flash("Company name is required.", "danger")
            return redirect(url_for("applications.add_application"))

        if not position:
            flash("Position is required.", "danger")
            return redirect(url_for("applications.add_application"))

        if status not in STATUSES:
            flash("Invalid application status.", "danger")
            return redirect(url_for("applications.add_application"))

        parsed_date = None

        if applied_date:
            try:
                parsed_date = datetime.strptime(
                    applied_date,
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                flash("Invalid application date.", "danger")
                return redirect(
                    url_for("applications.add_application")
                )

        application = JobApplication(
            user_id=current_user.id,
            company=company,
            position=position,
            job_url=job_url or None,
            location=location or None,
            status=status,
            applied_date=parsed_date,
            notes=notes or None
        )

        db.session.add(application)
        db.session.commit()

        flash("Job application added successfully!", "success")

        return redirect(
            url_for("applications.list_applications")
        )

    return render_template(
        "applications/add.html",
        statuses=STATUSES
    )


@applications.route("/<int:application_id>/edit", methods=["GET", "POST"])
@login_required
def edit_application(application_id):

    application = JobApplication.query.filter_by(
        id=application_id,
        user_id=current_user.id
    ).first_or_404()

    if request.method == "POST":

        company = request.form.get("company", "").strip()
        position = request.form.get("position", "").strip()
        job_url = request.form.get("job_url", "").strip()
        location = request.form.get("location", "").strip()
        status = request.form.get("status", "Wishlist")
        applied_date = request.form.get("applied_date")
        notes = request.form.get("notes", "").strip()

        if not company:
            flash("Company name is required.", "danger")
            return redirect(
                url_for(
                    "applications.edit_application",
                    application_id=application.id
                )
            )

        if not position:
            flash("Position is required.", "danger")
            return redirect(
                url_for(
                    "applications.edit_application",
                    application_id=application.id
                )
            )

        if status not in STATUSES:
            flash("Invalid application status.", "danger")
            return redirect(
                url_for(
                    "applications.edit_application",
                    application_id=application.id
                )
            )

        parsed_date = None

        if applied_date:
            try:
                parsed_date = datetime.strptime(
                    applied_date,
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                flash("Invalid application date.", "danger")
                return redirect(
                    url_for(
                        "applications.edit_application",
                        application_id=application.id
                    )
                )

        application.company = company
        application.position = position
        application.job_url = job_url or None
        application.location = location or None
        application.status = status
        application.applied_date = parsed_date
        application.notes = notes or None

        db.session.commit()

        flash("Job application updated successfully!", "success")

        return redirect(
            url_for("applications.list_applications")
        )

    return render_template(
        "applications/edit.html",
        application=application,
        statuses=STATUSES
    )


@applications.route(
    "/<int:application_id>/delete",
    methods=["POST"]
)
@login_required
def delete_application(application_id):

    application = JobApplication.query.filter_by(
        id=application_id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(application)
    db.session.commit()

    flash("Job application deleted successfully!", "success")

    return redirect(
        url_for("applications.list_applications")
    )