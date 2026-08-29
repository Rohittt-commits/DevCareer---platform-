from flask import Blueprint, render_template
from flask_login import login_required, current_user

from app.models.project import Project
from app.models.skill import Skill
from app.models.application import JobApplication
from app.models.goal import Goal
from app.models.learning import Learning

from app.services.career_intelligence import generate_career_insights
from app.services.github_service import GitHubService


main = Blueprint("main", __name__)


@main.route("/")
@login_required
def home():

    # ============================================================
    # PROJECT DATA
    # ============================================================

    projects = Project.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Project.updated_at.desc()
    ).all()

    project_count = len(projects)

    completed_projects = sum(
        1
        for project in projects
        if project.status
        and project.status.lower() == "completed"
    )

    in_progress_projects = sum(
        1
        for project in projects
        if project.status
        and project.status.lower() == "in progress"
    )

    planned_projects = sum(
        1
        for project in projects
        if project.status
        and project.status.lower() == "planned"
    )

    recent_projects = projects[:5]


    # ============================================================
    # SKILL DATA
    # ============================================================

    skills = Skill.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Skill.proficiency.desc()
    ).all()

    skill_count = len(skills)

    if skills:

        average_proficiency = round(
            sum(
                skill.proficiency
                for skill in skills
            ) / len(skills),
            1
        )

        strongest_skill = skills[0].name

        skills_needing_improvement = [
            skill
            for skill in skills
            if skill.proficiency <= 2
        ]

    else:

        average_proficiency = 0
        strongest_skill = None
        skills_needing_improvement = []

    top_skills = skills[:5]


    # ============================================================
    # APPLICATION DATA
    # ============================================================

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


    # ============================================================
    # APPLICATION METRICS
    # ============================================================

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


    # ============================================================
    # GOAL DATA
    # ============================================================

    goals = Goal.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Goal.updated_at.desc()
    ).all()

    goal_count = len(goals)

    active_goals = [
        goal
        for goal in goals
        if not goal.status
        or goal.status.lower() != "completed"
    ]

    completed_goals = [
        goal
        for goal in goals
        if goal.status
        and goal.status.lower() == "completed"
    ]

    if active_goals:

        average_goal_progress = round(
            sum(
                goal.progress
                for goal in active_goals
            ) / len(active_goals),
            1
        )

    else:

        average_goal_progress = 0

    recent_goals = goals[:5]


    # ============================================================
    # LEARNING DATA
    # ============================================================

    learning_items = Learning.query.filter_by(
        user_id=current_user.id
    ).order_by(
        Learning.updated_at.desc()
    ).all()

    learning_count = len(learning_items)

    active_learning = [
        item
        for item in learning_items
        if not item.status
        or item.status.lower() != "completed"
    ]

    completed_learning = [
        item
        for item in learning_items
        if item.status
        and item.status.lower() == "completed"
    ]

    if active_learning:

        average_learning_progress = round(
            sum(
                item.progress
                for item in active_learning
            ) / len(active_learning),
            1
        )

    else:

        average_learning_progress = 0

    recent_learning = learning_items[:5]


    # ============================================================
    # CAREER SCORE
    # ============================================================

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


    # ============================================================
    # CAREER INTELLIGENCE
    # ============================================================

    career_insights = generate_career_insights(
        current_user.id
    )


    # ============================================================
    # GITHUB DATA
    # ============================================================

    github_service = GitHubService()

    github_profile_result = github_service.get_profile()
    github_repositories_result = github_service.get_repositories()
    github_languages_result = github_service.get_language_summary()

    if github_profile_result.get("success"):

        github_profile = github_profile_result.get(
            "profile",
            {}
        )

    else:

        github_profile = None

    if github_repositories_result.get("success"):

        github_repositories = github_repositories_result.get(
            "repositories",
            []
        )

    else:

        github_repositories = []

    if github_languages_result.get("success"):

        github_languages = github_languages_result.get(
            "languages",
            []
        )

    else:

        github_languages = []

    github_connected = bool(github_profile)


    # ============================================================
    # DASHBOARD
    # ============================================================

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

        # Goals
        goals=goals,
        goal_count=goal_count,
        active_goals=active_goals,
        completed_goals=completed_goals,
        average_goal_progress=average_goal_progress,
        recent_goals=recent_goals,

        # Learning
        learning_items=learning_items,
        learning_count=learning_count,
        active_learning=active_learning,
        completed_learning=completed_learning,
        average_learning_progress=average_learning_progress,
        recent_learning=recent_learning,

        # Career
        career_score=career_score,

        # Intelligence
        career_insights=career_insights,

        # GitHub
        github_connected=github_connected,
        github_profile=github_profile,
        github_repositories=github_repositories,
        github_languages=github_languages
    )