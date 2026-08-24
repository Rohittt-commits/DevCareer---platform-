from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models.learning import Learning


learning = Blueprint("learning", __name__, url_prefix="/learning")


@learning.route("/")
@login_required
def list_learning():
    learning_items = Learning.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Learning.updated_at.desc()
    ).all()

    return render_template(
        "learning/list.html",
        learning_items=learning_items
    )


@learning.route("/create", methods=["GET", "POST"])
@login_required
def create_learning():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        category = request.form.get("category", "").strip()
        description = request.form.get("description", "").strip()
        resource_url = request.form.get("resource_url", "").strip()
        status = request.form.get("status", "Not Started").strip()
        notes = request.form.get("notes", "").strip()

        progress_raw = request.form.get("progress", "0").strip()

        if not title:
            flash("Learning title is required.", "error")
            return render_template("learning/create.html")

        try:
            progress = int(progress_raw)
        except ValueError:
            flash("Progress must be a number between 0 and 100.", "error")
            return render_template("learning/create.html")

        progress = max(0, min(progress, 100))

        start_date = None
        completion_date = None

        start_date_raw = request.form.get("start_date", "").strip()
        completion_date_raw = request.form.get(
            "completion_date",
            ""
        ).strip()

        if start_date_raw:
            try:
                start_date = datetime.strptime(
                    start_date_raw,
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                flash("Invalid start date.", "error")
                return render_template("learning/create.html")

        if completion_date_raw:
            try:
                completion_date = datetime.strptime(
                    completion_date_raw,
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                flash("Invalid completion date.", "error")
                return render_template("learning/create.html")

        learning_item = Learning(
            user_id=current_user.id,
            title=title,
            category=category or None,
            description=description or None,
            resource_url=resource_url or None,
            progress=progress,
            status=status or "Not Started",
            start_date=start_date,
            completion_date=completion_date,
            notes=notes or None
        )

        db.session.add(learning_item)
        db.session.commit()

        flash("Learning item created successfully.", "success")

        return redirect(
            url_for("learning.list_learning")
        )

    return render_template("learning/create.html")


@learning.route("/<int:learning_id>")
@login_required
def detail_learning(learning_id):
    learning_item = Learning.query.filter_by(
        id=learning_id,
        user_id=current_user.id
    ).first_or_404()

    return render_template(
        "learning/detail.html",
        learning_item=learning_item
    )


@learning.route("/<int:learning_id>/edit", methods=["GET", "POST"])
@login_required
def edit_learning(learning_id):
    learning_item = Learning.query.filter_by(
        id=learning_id,
        user_id=current_user.id
    ).first_or_404()

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        category = request.form.get("category", "").strip()
        description = request.form.get("description", "").strip()
        resource_url = request.form.get("resource_url", "").strip()
        status = request.form.get("status", "Not Started").strip()
        notes = request.form.get("notes", "").strip()

        progress_raw = request.form.get("progress", "0").strip()

        if not title:
            flash("Learning title is required.", "error")
            return render_template(
                "learning/edit.html",
                learning_item=learning_item
            )

        try:
            progress = int(progress_raw)
        except ValueError:
            flash("Progress must be a number between 0 and 100.", "error")
            return render_template(
                "learning/edit.html",
                learning_item=learning_item
            )

        progress = max(0, min(progress, 100))

        start_date = None
        completion_date = None

        start_date_raw = request.form.get("start_date", "").strip()
        completion_date_raw = request.form.get(
            "completion_date",
            ""
        ).strip()

        if start_date_raw:
            try:
                start_date = datetime.strptime(
                    start_date_raw,
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                flash("Invalid start date.", "error")
                return render_template(
                    "learning/edit.html",
                    learning_item=learning_item
                )

        if completion_date_raw:
            try:
                completion_date = datetime.strptime(
                    completion_date_raw,
                    "%Y-%m-%d"
                ).date()
            except ValueError:
                flash("Invalid completion date.", "error")
                return render_template(
                    "learning/edit.html",
                    learning_item=learning_item
                )

        learning_item.title = title
        learning_item.category = category or None
        learning_item.description = description or None
        learning_item.resource_url = resource_url or None
        learning_item.progress = progress
        learning_item.status = status or "Not Started"
        learning_item.start_date = start_date
        learning_item.completion_date = completion_date
        learning_item.notes = notes or None

        db.session.commit()

        flash("Learning item updated successfully.", "success")

        return redirect(
            url_for(
                "learning.detail_learning",
                learning_id=learning_item.id
            )
        )

    return render_template(
        "learning/edit.html",
        learning_item=learning_item
    )


@learning.route("/<int:learning_id>/delete", methods=["POST"])
@login_required
def delete_learning(learning_id):
    learning_item = Learning.query.filter_by(
        id=learning_id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(learning_item)
    db.session.commit()

    flash("Learning item deleted successfully.", "success")

    return redirect(
        url_for("learning.list_learning")
    )