from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models.project import Project


projects = Blueprint(
    "projects",
    __name__,
    url_prefix="/projects"
)


@projects.route("/")
@login_required
def list_projects():
    user_projects = Project.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Project.created_at.desc()
    ).all()

    return render_template(
        "projects.html",
        projects=user_projects
    )


@projects.route("/add", methods=["GET", "POST"])
@login_required
def add_project():
    if request.method == "POST":
        title = request.form.get("title")
        description = request.form.get("description")
        tech_stack = request.form.get("tech_stack")
        github_url = request.form.get("github_url")
        live_url = request.form.get("live_url")
        status = request.form.get("status")

        if not title or not description or not tech_stack:
            flash(
                "Title, description and tech stack are required.",
                "error"
            )
            return redirect(url_for("projects.add_project"))

        project = Project(
            title=title,
            description=description,
            tech_stack=tech_stack,
            github_url=github_url,
            live_url=live_url,
            status=status or "In Progress",
            user_id=current_user.id
        )

        db.session.add(project)
        db.session.commit()

        flash("Project added successfully!", "success")
        return redirect(url_for("projects.list_projects"))

    return render_template("add_project.html")


@projects.route("/edit/<int:project_id>", methods=["GET", "POST"])
@login_required
def edit_project(project_id):
    project = Project.query.filter_by(
        id=project_id,
        user_id=current_user.id
    ).first_or_404()

    if request.method == "POST":
        project.title = request.form.get("title")
        project.description = request.form.get("description")
        project.tech_stack = request.form.get("tech_stack")
        project.github_url = request.form.get("github_url")
        project.live_url = request.form.get("live_url")
        project.status = request.form.get("status") or "In Progress"

        db.session.commit()

        flash("Project updated successfully!", "success")
        return redirect(url_for("projects.list_projects"))

    return render_template(
        "edit_project.html",
        project=project
    )


@projects.route("/delete/<int:project_id>", methods=["POST"])
@login_required
def delete_project(project_id):
    project = Project.query.filter_by(
        id=project_id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(project)
    db.session.commit()

    flash("Project deleted successfully.", "success")
    return redirect(url_for("projects.list_projects"))