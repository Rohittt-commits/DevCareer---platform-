from app.models.project import Project
from app.models.skill import Skill
from app.models.application import JobApplication
from app.models.goal import Goal
from app.models.learning import Learning


def generate_career_insights(user_id):
    """
    Generate career insights based on the user's
    current DevCareer data.
    """

    projects = Project.query.filter_by(user_id=user_id).all()
    skills = Skill.query.filter_by(user_id=user_id).all()
    applications = JobApplication.query.filter_by(user_id=user_id).all()
    goals = Goal.query.filter_by(user_id=user_id).all()
    learning_items = Learning.query.filter_by(user_id=user_id).all()

    completed_projects = [
        project
        for project in projects
        if project.status
        and project.status.lower() == "completed"
    ]

    if len(completed_projects) == 0:
        project_insight = {
            "type": "portfolio",
            "title": "Build Your First Strong Project",
            "message": (
                "You do not have any completed projects yet. "
                "Build and complete a practical project that "
                "demonstrates your development skills."
            ),
            "priority": "high"
        }

    elif len(completed_projects) < 2:
        project_insight = {
            "type": "portfolio",
            "title": "Strengthen Your Portfolio",
            "message": (
                "You have started building your portfolio. "
                "Try to complete at least one more strong project "
                "with clear documentation and real-world functionality."
            ),
            "priority": "medium"
        }

    else:
        project_insight = {
            "type": "portfolio",
            "title": "Portfolio Is Building Well",
            "message": (
                f"You currently have {len(completed_projects)} "
                "completed projects. Keep improving them and "
                "highlight measurable results in your portfolio."
            ),
            "priority": "low"
        }

    weak_skills = [
        skill
        for skill in skills
        if skill.proficiency is not None
        and skill.proficiency <= 2
    ]

    if weak_skills:
        weakest_skill = min(
            weak_skills,
            key=lambda skill: skill.proficiency
        )

        skill_insight = {
            "type": "skill",
            "title": "Skill Needs Improvement",
            "message": (
                f"{weakest_skill.name} is currently one of your "
                "weakest skills. Practice it through projects, "
                "exercises and practical development."
            ),
            "priority": "high"
        }

    elif not skills:
        skill_insight = {
            "type": "skill",
            "title": "Start Tracking Your Skills",
            "message": (
                "Add the technical skills you are currently learning "
                "or using so DevCareer can provide better career insights."
            ),
            "priority": "medium"
        }

    else:
        skill_insight = {
            "type": "skill",
            "title": "Keep Improving Your Skills",
            "message": (
                "Your current skills are being tracked. Continue "
                "improving proficiency and apply your skills in "
                "real projects."
            ),
            "priority": "low"
        }

    applied_statuses = {
        "Applied",
        "Assessment",
        "Interview",
        "Offer",
        "Rejected"
    }

    applied_applications = [
        application
        for application in applications
        if application.status in applied_statuses
    ]

    interviews = [
        application
        for application in applications
        if application.status == "Interview"
    ]

    offers = [
        application
        for application in applications
        if application.status == "Offer"
    ]

    if len(applied_applications) == 0:
        application_insight = {
            "type": "applications",
            "title": "Start Applying Consistently",
            "message": (
                "You have not tracked any active job applications yet. "
                "Start applying to relevant internships or jobs and "
                "track them inside DevCareer."
            ),
            "priority": "high"
        }

    elif len(applied_applications) < 5:
        application_insight = {
            "type": "applications",
            "title": "Increase Application Activity",
            "message": (
                f"You have tracked {len(applied_applications)} "
                "applications. Increase your application activity "
                "while focusing on opportunities that match your skills."
            ),
            "priority": "medium"
        }

    elif interviews:
        application_insight = {
            "type": "applications",
            "title": "Interview Opportunities Are Growing",
            "message": (
                f"You currently have {len(interviews)} application(s) "
                "at the interview stage. Focus on interview preparation "
                "and researching each company."
            ),
            "priority": "medium"
        }

    elif offers:
        application_insight = {
            "type": "applications",
            "title": "You Have an Offer",
            "message": (
                f"You currently have {len(offers)} offer(s) tracked. "
                "Review the opportunities carefully and keep your "
                "application pipeline updated."
            ),
            "priority": "low"
        }

    else:
        application_insight = {
            "type": "applications",
            "title": "Keep Applying",
            "message": (
                f"You have tracked {len(applied_applications)} "
                "applications. Continue applying consistently and "
                "monitor your application pipeline."
            ),
            "priority": "low"
        }

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
        learning_insight = {
            "type": "learning",
            "title": "Continue Your Learning",
            "message": (
                f"You currently have {len(active_learning)} "
                "active learning item(s). Keep making progress "
                "and convert important learning into practical work."
            ),
            "priority": "medium"
        }

    elif not learning_items:
        learning_insight = {
            "type": "learning",
            "title": "Track Your Learning",
            "message": (
                "Add courses, technologies or learning goals to "
                "your learning tracker so DevCareer can monitor "
                "your progress."
            ),
            "priority": "medium"
        }

    else:
        learning_insight = {
            "type": "learning",
            "title": "Learning Progress Is Strong",
            "message": (
                f"You have completed {len(completed_learning)} "
                "learning item(s). Keep applying what you learn "
                "through practical projects."
            ),
            "priority": "low"
        }

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
        lowest_goal = min(
            active_goals,
            key=lambda goal: goal.progress or 0
        )

        goal_insight = {
            "type": "goals",
            "title": "Focus On Your Lowest Progress Goal",
            "message": (
                f"Your goal '{lowest_goal.title}' is currently at "
                f"{lowest_goal.progress or 0}% progress. "
                "Give it focused attention this week."
            ),
            "priority": "medium"
        }

    elif not goals:
        goal_insight = {
            "type": "goals",
            "title": "Set Your First Career Goal",
            "message": (
                "Create a measurable career goal to give your "
                "development journey a clear direction."
            ),
            "priority": "medium"
        }

    else:
        goal_insight = {
            "type": "goals",
            "title": "Goals Completed",
            "message": (
                f"You have completed {len(completed_goals)} goal(s). "
                "Set your next career milestone to keep moving forward."
            ),
            "priority": "low"
        }

    return [
        project_insight,
        skill_insight,
        application_insight,
        learning_insight,
        goal_insight
    ]


def generate_career_action(user_id):
    """
    Generate one highest-priority career action
    based on the user's current DevCareer data.
    """

    projects = Project.query.filter_by(user_id=user_id).all()
    skills = Skill.query.filter_by(user_id=user_id).all()
    applications = JobApplication.query.filter_by(user_id=user_id).all()
    goals = Goal.query.filter_by(user_id=user_id).all()
    learning_items = Learning.query.filter_by(user_id=user_id).all()

    weak_skills = [
        skill
        for skill in skills
        if skill.proficiency is not None
        and skill.proficiency <= 2
    ]

    if weak_skills:
        weakest_skill = min(
            weak_skills,
            key=lambda skill: skill.proficiency
        )

        return {
            "title": "Strengthen Your Weakest Skill",
            "priority": "high",
            "action": (
                f"Improve {weakest_skill.name} and use it "
                f"in a practical project."
            )
        }

    active_learning = [
        item
        for item in learning_items
        if not item.status
        or item.status.lower() != "completed"
    ]

    if active_learning and not projects:
        return {
            "title": "Turn Learning Into a Project",
            "priority": "high",
            "action": (
                "Build a practical project around what you are "
                "currently learning to strengthen your portfolio."
            )
        }

    completed_projects = [
        project
        for project in projects
        if project.status
        and project.status.lower() == "completed"
    ]

    if len(completed_projects) < 2:
        return {
            "title": "Strengthen Your Portfolio",
            "priority": "high",
            "action": (
                "Complete at least two strong projects and "
                "document the technologies and results."
            )
        }

    applied_statuses = {
        "Applied",
        "Assessment",
        "Interview",
        "Offer",
        "Rejected"
    }

    applied_applications = [
        application
        for application in applications
        if application.status in applied_statuses
    ]

    if len(applied_applications) < 5:
        return {
            "title": "Increase Your Application Activity",
            "priority": "medium",
            "action": (
                "Apply to more relevant opportunities and "
                "track every application inside DevCareer."
            )
        }

    active_goals = [
        goal
        for goal in goals
        if not goal.status
        or goal.status.lower() != "completed"
    ]

    if active_goals:
        lowest_goal = min(
            active_goals,
            key=lambda goal: goal.progress or 0
        )

        return {
            "title": "Make Progress On Your Goal",
            "priority": "medium",
            "action": (
                f"Focus on your goal '{lowest_goal.title}' "
                f"and move its progress beyond "
                f"{lowest_goal.progress or 0}%."
            )
        }

    return {
        "title": "Keep Building Momentum",
        "priority": "low",
        "action": (
            "Keep your projects, skills, learning and "
            "job applications updated to maintain accurate "
            "career insights."
        )
    }

