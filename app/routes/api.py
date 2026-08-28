from flask import Blueprint, jsonify
from flask_login import login_required, current_user

from app.models.project import Project
from app.models.skill import Skill
from app.models.application import JobApplication
from app.models.goal import Goal
from app.models.learning import Learning


api = Blueprint(
    "api",
    __name__,
    url_prefix="/api"
)


@api.route("/dashboard")
@login_required
def dashboard():

    projects = Project.query.filter_by(
        user_id=current_user.id
    ).all()

    skills = Skill.query.filter_by(
        user_id=current_user.id
    ).all()

    applications = JobApplication.query.filter_by(
        user_id=current_user.id
    ).all()

    goals = Goal.query.filter_by(
        user_id=current_user.id
    ).all()

    learning_items = Learning.query.filter_by(
        user_id=current_user.id
    ).all()

    return jsonify({
        "success": True,
        "user": {
            "id": current_user.id,
            "username": current_user.username,
            "email": current_user.email
        },
        "statistics": {
            "projects": len(projects),
            "skills": len(skills),
            "applications": len(applications),
            "goals": len(goals),
            "learning": len(learning_items)
        }
    })


@api.route("/projects")
@login_required
def projects():

    projects = Project.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Project.updated_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(projects),
        "projects": [
            {
                "id": project.id,
                "title": project.title,
                "status": project.status
            }
            for project in projects
        ]
    })


@api.route("/skills")
@login_required
def skills():

    skills = Skill.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Skill.proficiency.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(skills),
        "skills": [
            {
                "id": skill.id,
                "name": skill.name,
                "category": skill.category,
                "proficiency": skill.proficiency,
                "experience_months": skill.experience_months
            }
            for skill in skills
        ]
    })


@api.route("/applications")
@login_required
def applications():

    applications = JobApplication.query.filter_by(
        user_id=current_user.id
    ).order_by(
        JobApplication.created_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(applications),
        "applications": [
            {
                "id": application.id,
                "company": application.company,
                "position": application.position,
                "location": application.location,
                "status": application.status,
                "applied_date": (
                    application.applied_date.isoformat()
                    if application.applied_date
                    else None
                )
            }
            for application in applications
        ]
    })


@api.route("/goals")
@login_required
def goals():

    goals = Goal.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Goal.updated_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(goals),
        "goals": [
            {
                "id": goal.id,
                "title": goal.title,
                "category": goal.category,
                "status": goal.status,
                "progress": goal.progress,
                "target_date": (
                    goal.target_date.isoformat()
                    if goal.target_date
                    else None
                )
            }
            for goal in goals
        ]
    })


@api.route("/learning")
@login_required
def learning():

    learning_items = Learning.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Learning.updated_at.desc()
    ).all()

    return jsonify({
        "success": True,
        "count": len(learning_items),
        "learning": [
            {
                "id": item.id,
                "title": item.title,
                "category": item.category,
                "progress": item.progress,
                "status": item.status,
                "resource_url": item.resource_url
            }
            for item in learning_items
        ]
    })