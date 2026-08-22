from datetime import datetime

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models.goal import Goal


goals = Blueprint(
    "goals",
    __name__,
    url_prefix="/goals"
)


# =========================
# LIST GOALS
# =========================

@goals.route("/")
@login_required
def list_goals():

    user_goals = Goal.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Goal.updated_at.desc()
    ).all()

    return render_template(
        "goals/list.html",
        goals=user_goals
    )


# =========================
# CREATE GOAL
# =========================

@goals.route("/create", methods=["GET", "POST"])
@login_required
def create_goal():

    if request.method == "POST":

        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        category = request.form.get("category", "").strip()
        target_date = request.form.get("target_date", "").strip()

        if not title:

            flash(
                "Goal title is required.",
                "error"
            )

            return render_template(
                "goals/create.html"
            )

        goal = Goal(
            user_id=current_user.id,
            title=title,
            description=description or None,
            category=category or None,
            status="Not Started",
            progress=0
        )

        if target_date:

            try:

                goal.target_date = datetime.strptime(
                    target_date,
                    "%Y-%m-%d"
                ).date()

            except ValueError:

                flash(
                    "Please enter a valid target date.",
                    "error"
                )

                return render_template(
                    "goals/create.html"
                )

        db.session.add(goal)

        db.session.commit()

        flash(
            "Goal created successfully!",
            "success"
        )

        return redirect(
            url_for("goals.list_goals")
        )

    return render_template(
        "goals/create.html"
    )


# =========================
# VIEW GOAL
# =========================

@goals.route("/<int:goal_id>")
@login_required
def goal_detail(goal_id):

    goal = Goal.query.filter_by(
        id=goal_id,
        user_id=current_user.id
    ).first_or_404()

    return render_template(
        "goals/detail.html",
        goal=goal
    )


# =========================
# EDIT GOAL
# =========================

@goals.route("/<int:goal_id>/edit", methods=["GET", "POST"])
@login_required
def edit_goal(goal_id):

    goal = Goal.query.filter_by(
        id=goal_id,
        user_id=current_user.id
    ).first_or_404()

    if request.method == "POST":

        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        category = request.form.get("category", "").strip()
        target_date = request.form.get("target_date", "").strip()
        status = request.form.get(
            "status",
            "Not Started"
        ).strip()

        progress_value = request.form.get(
            "progress",
            "0"
        ).strip()

        if not title:

            flash(
                "Goal title is required.",
                "error"
            )

            return render_template(
                "goals/edit.html",
                goal=goal
            )

        try:

            progress = int(progress_value)

        except ValueError:

            flash(
                "Progress must be a number between 0 and 100.",
                "error"
            )

            return render_template(
                "goals/edit.html",
                goal=goal
            )

        if progress < 0 or progress > 100:

            flash(
                "Progress must be between 0 and 100.",
                "error"
            )

            return render_template(
                "goals/edit.html",
                goal=goal
            )

        goal.title = title

        goal.description = (
            description
            if description
            else None
        )

        goal.category = (
            category
            if category
            else None
        )

        goal.status = status

        goal.progress = progress

        if target_date:

            try:

                goal.target_date = datetime.strptime(
                    target_date,
                    "%Y-%m-%d"
                ).date()

            except ValueError:

                flash(
                    "Please enter a valid target date.",
                    "error"
                )

                return render_template(
                    "goals/edit.html",
                    goal=goal
                )

        else:

            goal.target_date = None

        db.session.commit()

        flash(
            "Goal updated successfully!",
            "success"
        )

        return redirect(
            url_for(
                "goals.goal_detail",
                goal_id=goal.id
            )
        )

    return render_template(
        "goals/edit.html",
        goal=goal
    )


# =========================
# DELETE GOAL
# =========================

@goals.route("/<int:goal_id>/delete", methods=["POST"])
@login_required
def delete_goal(goal_id):

    goal = Goal.query.filter_by(
        id=goal_id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(goal)

    db.session.commit()

    flash(
        "Goal deleted successfully.",
        "success"
    )

    return redirect(
        url_for("goals.list_goals")
    )