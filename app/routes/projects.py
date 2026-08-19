from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user

from app import db
from app.models.project import Project


projects = Blueprint("projects", __name__, url_prefix="/projects")


@projects.route("/")
@login_required
def list_projects():
    projects_list = Project.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Project.created_at.desc()
    ).all()

    return render_template(
        "projects/list.html",
        projects=projects_list
    )


@projects.route("/create", methods=["GET", "POST"])
@login_required
def create_project():
    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        technologies = request.form.get("technologies", "").strip()
        github_url = request.form.get("github_url", "").strip()
        live_url = request.form.get("live_url", "").strip()
        status = request.form.get("status", "In Progress").strip()

        if not title:
            flash("Project title is required.", "danger")
            return render_template("projects/create.html")

        project = Project(
            user_id=current_user.id,
            title=title,
            description=description,
            technologies=technologies,
            github_url=github_url,
            live_url=live_url,
            status=status
        )

        db.session.add(project)
        db.session.commit()

        flash("Project created successfully!", "success")

        return redirect(url_for("projects.list_projects"))

    return render_template("projects/create.html")


@projects.route("/<int:project_id>")
@login_required
def project_detail(project_id):
    project = Project.query.filter_by(
        id=project_id,
        user_id=current_user.id
    ).first_or_404()

    return render_template(
        "projects/detail.html",
        project=project
    )


@projects.route("/<int:project_id>/edit", methods=["GET", "POST"])
@login_required
def edit_project(project_id):
    project = Project.query.filter_by(
        id=project_id,
        user_id=current_user.id
    ).first_or_404()

    if request.method == "POST":
        title = request.form.get("title", "").strip()
        description = request.form.get("description", "").strip()
        technologies = request.form.get("technologies", "").strip()
        github_url = request.form.get("github_url", "").strip()
        live_url = request.form.get("live_url", "").strip()
        status = request.form.get("status", "In Progress").strip()

        if not title:
            flash("Project title is required.", "danger")
            return render_template(
                "projects/edit.html",
                project=project
            )

        project.title = title
        project.description = description
        project.technologies = technologies
        project.github_url = github_url
        project.live_url = live_url
        project.status = status

        db.session.commit()

        flash("Project updated successfully!", "success")

        return redirect(
            url_for(
                "projects.project_detail",
                project_id=project.id
            )
        )

    return render_template(
        "projects/edit.html",
        project=project
    )


@projects.route("/<int:project_id>/delete", methods=["POST"])
@login_required
def delete_project(project_id):
    project = Project.query.filter_by(
        id=project_id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(project)
    db.session.commit()

    flash("Project deleted successfully!", "success")

    return redirect(url_for("projects.list_projects"))