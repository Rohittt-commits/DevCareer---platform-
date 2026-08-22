from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.project import Project
from app.models.skill import Skill
from app.models.application import JobApplication


main = Blueprint("main", __name__)


@main.route("/")
@login_required
def home():

    # =========================
    # PROJECT DATA
    # =========================

    projects = Project.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Project.updated_at.desc()
    ).all()

    project_count = len(projects)

    completed_projects = sum(
        1 for project in projects
        if project.status.lower() == "completed"
    )

    in_progress_projects = sum(
        1 for project in projects
        if project.status.lower() == "in progress"
    )

    planned_projects = sum(
        1 for project in projects
        if project.status.lower() == "planned"
    )

    recent_projects = projects[:5]


    # =========================
    # SKILL DATA
    # =========================

    skills = Skill.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Skill.proficiency.desc()
    ).all()

    skill_count = len(skills)

    if skills:
        average_proficiency = round(
            sum(skill.proficiency for skill in skills) / len(skills),
            1
        )

        strongest_skill = skills[0].name

        skills_needing_improvement = [
            skill for skill in skills
            if skill.proficiency <= 2
        ]

    else:
        average_proficiency = 0
        strongest_skill = None
        skills_needing_improvement = []

    top_skills = skills[:5]


    # =========================
    # APPLICATION DATA
    # =========================

    applications = JobApplication.query.filter_by(
        user_id=current_user.id
    ).order_by(
        JobApplication.created_at.desc()
    ).all()

    application_count = len(applications)

    application_pipeline = {
        "Wishlist": 0,
        "Applied": 0,
        "Assessment": 0,
        "Interview": 0,
        "Offer": 0,
        "Rejected": 0,
        "Withdrawn": 0
    }

    for application in applications:

        if application.status in application_pipeline:

            application_pipeline[application.status] += 1


    applied_count = (
        application_pipeline["Applied"]
        + application_pipeline["Assessment"]
        + application_pipeline["Interview"]
        + application_pipeline["Offer"]
        + application_pipeline["Rejected"]
    )

    interview_count = application_pipeline["Interview"]

    offer_count = application_pipeline["Offer"]

    rejected_count = application_pipeline["Rejected"]


    # =========================
    # APPLICATION METRICS
    # =========================

    if applied_count > 0:

        interview_rate = round(
            (interview_count / applied_count) * 100,
            1
        )

        offer_rate = round(
            (offer_count / applied_count) * 100,
            1
        )

    else:

        interview_rate = 0

        offer_rate = 0


    recent_applications = applications[:5]


    # =========================
    # CAREER SCORE
    # =========================

    project_score = min(
        project_count * 10,
        30
    )

    skill_score = min(
        skill_count * 5,
        25
    )

    application_score = min(
        application_count * 5,
        20
    )

    proficiency_score = (
        average_proficiency / 5
    ) * 25

    career_score = round(
        project_score
        + skill_score
        + application_score
        + proficiency_score
    )

    career_score = min(
        career_score,
        100
    )


    # =========================
    # DASHBOARD
    # =========================

    return render_template(
        "dashboard.html",

        # Projects
        projects=projects,
        project_count=project_count,
        completed_projects=completed_projects,
        in_progress_projects=in_progress_projects,
        planned_projects=planned_projects,
        recent_projects=recent_projects,

        # Skills
        skills=skills,
        skill_count=skill_count,
        average_proficiency=average_proficiency,
        strongest_skill=strongest_skill,
        skills_needing_improvement=skills_needing_improvement,
        top_skills=top_skills,

        # Applications
        applications=applications,
        application_count=application_count,
        application_pipeline=application_pipeline,
        applied_count=applied_count,
        interview_count=interview_count,
        offer_count=offer_count,
        rejected_count=rejected_count,
        interview_rate=interview_rate,
        offer_rate=offer_rate,
        recent_applications=recent_applications,

        # Career
        career_score=career_score
    )