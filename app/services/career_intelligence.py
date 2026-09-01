from app.models.project import Project
from app.models.skill import Skill
from app.models.application import JobApplication
from app.models.goal import Goal
from app.models.learning import Learning


def generate_career_insights(user_id):
    """
    Generate personalized career insights based on
    the user's current DevCareer data.
    """

    projects = Project.query.filter_by(user_id=user_id).all()
    skills = Skill.query.filter_by(user_id=user_id).all()
    applications = JobApplication.query.filter_by(user_id=user_id).all()
    goals = Goal.query.filter_by(user_id=user_id).all()
    learning_items = Learning.query.filter_by(user_id=user_id).all()

    insights = []

    # ============================================================
    # PROJECT INSIGHT
    # ============================================================

    completed_projects = [
        project
        for project in projects
        if project.status
        and project.status.lower() == "completed"
    ]

    if len(completed_projects) == 0:
        insights.append({
            "type": "portfolio",
            "title": "Build Your First Strong Project",
            "message": (
                "You do not have any completed projects yet. "
                "Build and complete a practical project that "
                "demonstrates your development skills."
            ),
            "priority": "high"
        })

    elif len(completed_projects) < 2:
        insights.append({
            "type": "portfolio",
            "title": "Strengthen Your Portfolio",
            "message": (
                "You have started building your portfolio. "
                "Complete another strong project and document "
                "the technologies and results."
            ),
            "priority": "medium"
        })

    else:
        insights.append({
            "type": "portfolio",
            "title": "Portfolio Is Building Well",
            "message": (
                f"You currently have {len(completed_projects)} "
                "completed projects. Keep improving them and "
                "highlight measurable results."
            ),
            "priority": "low"
        })

    # ============================================================
    # SKILL INSIGHT
    # ============================================================

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

        insights.append({
            "type": "skill",
            "title": "Skill Needs Improvement",
            "message": (
                f"{weakest_skill.name} is currently one of your "
                "weakest skills. Practice it through projects "
                "and practical development."
            ),
            "priority": "high"
        })

    elif not skills:
        insights.append({
            "type": "skill",
            "title": "Start Tracking Your Skills",
            "message": (
                "Add the technical skills you are currently learning "
                "or using so DevCareer can provide better insights."
            ),
            "priority": "medium"
        })

    else:
        insights.append({
            "type": "skill",
            "title": "Keep Improving Your Skills",
            "message": (
                "Your technical skills are being tracked. Continue "
                "improving proficiency and applying those skills "
                "in real projects."
            ),
            "priority": "low"
        })

    # ============================================================
    # APPLICATION INSIGHT
    # ============================================================

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
        insights.append({
            "type": "applications",
            "title": "Start Applying Consistently",
            "message": (
                "You have not tracked any active applications yet. "
                "Start applying to relevant internships or jobs "
                "and track them inside DevCareer."
            ),
            "priority": "high"
        })

    elif len(applied_applications) < 5:
        insights.append({
            "type": "applications",
            "title": "Increase Application Activity",
            "message": (
                f"You have tracked {len(applied_applications)} "
                "applications. Increase your activity while "
                "focusing on relevant opportunities."
            ),
            "priority": "medium"
        })

    elif interviews:
        insights.append({
            "type": "applications",
            "title": "Interview Opportunities Are Growing",
            "message": (
                f"You currently have {len(interviews)} application(s) "
                "at the interview stage. Focus on interview preparation."
            ),
            "priority": "medium"
        })

    elif offers:
        insights.append({
            "type": "applications",
            "title": "You Have an Offer",
            "message": (
                f"You currently have {len(offers)} offer(s) tracked. "
                "Keep your application pipeline updated."
            ),
            "priority": "low"
        })

    else:
        insights.append({
            "type": "applications",
            "title": "Keep Applying",
            "message": (
                f"You have tracked {len(applied_applications)} "
                "applications. Continue applying consistently."
            ),
            "priority": "low"
        })

    # ============================================================
    # LEARNING INSIGHT
    # ============================================================

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
        insights.append({
            "type": "learning",
            "title": "Continue Your Learning",
            "message": (
                f"You currently have {len(active_learning)} "
                "active learning item(s). Convert important learning "
                "into practical work."
            ),
            "priority": "medium"
        })

    elif not learning_items:
        insights.append({
            "type": "learning",
            "title": "Track Your Learning",
            "message": (
                "Add courses, technologies or learning goals so "
                "DevCareer can monitor your progress."
            ),
            "priority": "medium"
        })

    else:
        insights.append({
            "type": "learning",
            "title": "Learning Progress Is Strong",
            "message": (
                f"You have completed {len(completed_learning)} "
                "learning item(s). Keep applying what you learn."
            ),
            "priority": "low"
        })

    # ============================================================
    # GOAL INSIGHT
    # ============================================================

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

        insights.append({
            "type": "goals",
            "title": "Focus On Your Lowest Progress Goal",
            "message": (
                f"Your goal '{lowest_goal.title}' is currently at "
                f"{lowest_goal.progress or 0}% progress. Give it "
                "focused attention."
            ),
            "priority": "medium"
        })

    elif not goals:
        insights.append({
            "type": "goals",
            "title": "Set Your First Career Goal",
            "message": (
                "Create a measurable career goal to give your "
                "development journey a clear direction."
            ),
            "priority": "medium"
        })

    else:
        insights.append({
            "type": "goals",
            "title": "Goals Completed",
            "message": (
                f"You have completed {len(completed_goals)} goal(s). "
                "Set your next career milestone."
            ),
            "priority": "low"
        })

    return insights


def generate_career_action(user_id):
    """
    Generate the single highest-priority career action.
    """

    projects = Project.query.filter_by(user_id=user_id).all()
    skills = Skill.query.filter_by(user_id=user_id).all()
    applications = JobApplication.query.filter_by(user_id=user_id).all()
    goals = Goal.query.filter_by(user_id=user_id).all()
    learning_items = Learning.query.filter_by(user_id=user_id).all()

    # Weak skill
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
                "in a practical project."
            )
        }

    # Learning without projects
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

    # Portfolio
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

    # Applications
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

    # Goals
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
                f"Focus on '{lowest_goal.title}' and move its "
                f"progress beyond {lowest_goal.progress or 0}%."
            )
        }

    return {
        "title": "Keep Building Momentum",
        "priority": "low",
        "action": (
            "Keep your projects, skills, learning and applications "
            "updated to maintain accurate career insights."
        )
    }


def generate_career_health(user_id):
    """
    Calculate measurable career-health dimensions.
    Each category is scored from 0 to 100.
    """

    projects = Project.query.filter_by(user_id=user_id).all()
    skills = Skill.query.filter_by(user_id=user_id).all()
    applications = JobApplication.query.filter_by(user_id=user_id).all()
    goals = Goal.query.filter_by(user_id=user_id).all()
    learning_items = Learning.query.filter_by(user_id=user_id).all()

    # ------------------------------------------------------------
    # PORTFOLIO HEALTH
    # ------------------------------------------------------------

    completed_projects = [
        project
        for project in projects
        if project.status
        and project.status.lower() == "completed"
    ]

    portfolio_score = min(
        len(completed_projects) * 25,
        100
    )

    # ------------------------------------------------------------
    # SKILL HEALTH
    # ------------------------------------------------------------

    if skills:
        valid_proficiencies = [
            skill.proficiency
            for skill in skills
            if skill.proficiency is not None
        ]

        if valid_proficiencies:
            average_skill = sum(valid_proficiencies) / len(
                valid_proficiencies
            )

            skill_score = round(
                (average_skill / 5) * 100
            )
        else:
            skill_score = 0
    else:
        skill_score = 0

    # ------------------------------------------------------------
    # APPLICATION HEALTH
    # ------------------------------------------------------------

    applied_statuses = {
        "Applied",
        "Assessment",
        "Interview",
        "Offer",
        "Rejected"
    }

    applied_count = sum(
        1
        for application in applications
        if application.status in applied_statuses
    )

    application_score = min(
        applied_count * 10,
        100
    )

    # ------------------------------------------------------------
    # LEARNING HEALTH
    # ------------------------------------------------------------

    if learning_items:
        progress_values = [
            item.progress or 0
            for item in learning_items
        ]

        learning_score = round(
            sum(progress_values) / len(progress_values)
        )
    else:
        learning_score = 0

    # ------------------------------------------------------------
    # GOAL HEALTH
    # ------------------------------------------------------------

    if goals:
        progress_values = [
            goal.progress or 0
            for goal in goals
        ]

        goal_score = round(
            sum(progress_values) / len(progress_values)
        )
    else:
        goal_score = 0

    # ------------------------------------------------------------
    # OVERALL HEALTH
    # ------------------------------------------------------------

    overall_score = round(
        (
            portfolio_score
            + skill_score
            + application_score
            + learning_score
            + goal_score
        ) / 5
    )

    return {
        "overall": min(overall_score, 100),
        "portfolio": portfolio_score,
        "skills": skill_score,
        "applications": application_score,
        "learning": learning_score,
        "goals": goal_score
    }