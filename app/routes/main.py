from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.project import Project
from app.models.skill import Skill


main = Blueprint("main", __name__)


@main.route("/")
@login_required
def home():
    projects = Project.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Project.updated_at.desc()
    ).all()

    skills = Skill.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Skill.proficiency.desc()
    ).all()

    project_count = len(projects)
    skill_count = len(skills)

    recent_projects = projects[:5]
    top_skills = skills[:5]

    return render_template(
        "dashboard.html",
        projects=projects,
        skills=skills,
        project_count=project_count,
        skill_count=skill_count,
        recent_projects=recent_projects,
        top_skills=top_skills
    )