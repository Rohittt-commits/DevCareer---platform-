from datetime import date

from app.models.project import Project
from app.models.skill import Skill
from app.models.application import JobApplication
from app.models.goal import Goal
from app.models.learning import Learning


def generate_career_insights(user_id):
    """
    Analyze a user's DevCareer data and return
    actionable career insights.
    """

    # ============================================================
    # FETCH USER DATA
    # ============================================================

    projects = Project.query.filter_by(
        user_id=user_id
    ).all()

    skills = Skill.query.filter_by(
        user_id=user_id
    ).all()

    applications = JobApplication.query.filter_by(
        user_id=user_id
    ).all()

    goals = Goal.query.filter_by(
        user_id=user_id
    ).all()

    learning_items = Learning.query.filter_by(
        user_id=user_id
    ).all()

    insights = []


    # ============================================================
    # PROJECT INSIGHTS
    # ============================================================

    project_count = len(projects)

    completed_projects = [
        project
        for project in projects
        if project.status
        and project.status.lower() == "completed"
    ]

    in_progress_projects = [
        project
        for project in projects
        if project.status
        and project.status.lower() == "in progress"
    ]

    if project_count == 0:

        insights.append({
            "type": "project",
            "priority": "high",
            "title": "Start your project portfolio",
            "message": (
                "Add your first project to begin building "
                "your developer portfolio."
            )
        })

    elif len(completed_projects) == 0:

        insights.append({
            "type": "project",
            "priority": "high",
            "title": "Complete a project",
            "message": (
                "You have projects in your portfolio, but none "
                "are marked as completed. Finishing a project "
                "will strengthen your portfolio."
            )
        })

    elif in_progress_projects:

        insights.append({
            "type": "project",
            "priority": "medium",
            "title": "Finish an active project",
            "message": (
                f"You have {len(in_progress_projects)} project(s) "
                "currently in progress. Consider completing one "
                "before starting another."
            )
        })

    else:

        insights.append({
            "type": "project",
            "priority": "low",
            "title": "Keep building",
            "message": (
                f"You have {len(completed_projects)} completed "
                "project(s). Consider adding another project "
                "that demonstrates a new backend skill."
            )
        })


    # ============================================================
    # SKILL INSIGHTS
    # ============================================================

    skill_count = len(skills)

    if skill_count == 0:

        insights.append({
            "type": "skill",
            "priority": "high",
            "title": "Build your skill profile",
            "message": (
                "Add the technologies and skills you are currently "
                "learning or using."
            )
        })

    else:

        strongest_skill = max(
            skills,
            key=lambda skill: skill.proficiency
        )

        weak_skills = [
            skill
            for skill in skills
            if skill.proficiency <= 2
        ]

        insights.append({
            "type": "skill",
            "priority": "low",
            "title": "Strongest skill",
            "message": (
                f"{strongest_skill.name} is currently your strongest "
                f"skill with a proficiency of "
                f"{strongest_skill.proficiency}/5."
            )
        })

        if weak_skills:

            insights.append({
                "type": "skill",
                "priority": "medium",
                "title": "Skills to improve",
                "message": (
                    f"You have {len(weak_skills)} skill(s) with "
                    "proficiency of 2/5 or below. Consider focusing "
                    "your learning time on these areas."
                )
            })


    # ============================================================
    # APPLICATION INSIGHTS
    # ============================================================

    application_count = len(applications)

    applied_applications = [
        application
        for application in applications
        if application.status in [
            "Applied",
            "Assessment",
            "Interview",
            "Offer",
            "Rejected"
        ]
    ]

    interview_applications = [
        application
        for application in applications
        if application.status == "Interview"
    ]

    offer_applications = [
        application
        for application in applications
        if application.status == "Offer"
    ]

    if application_count == 0:

        insights.append({
            "type": "application",
            "priority": "high",
            "title": "Start tracking opportunities",
            "message": (
                "Add job applications to track your job search "
                "pipeline and measure your progress."
            )
        })

    elif len(applied_applications) == 0:

        insights.append({
            "type": "application",
            "priority": "high",
            "title": "Move from wishlist to applications",
            "message": (
                "You have opportunities saved, but no recorded "
                "applications yet. Start applying to suitable roles."
            )
        })

    else:

        interview_rate = round(
            (
                len(interview_applications)
                / len(applied_applications)
            ) * 100,
            1
        )

        if interview_rate < 10:

            insights.append({
                "type": "application",
                "priority": "high",
                "title": "Improve your application strategy",
                "message": (
                    f"Your current interview rate is {interview_rate}%. "
                    "Consider improving your resume, project portfolio "
                    "and application targeting."
                )
            })

        elif interview_rate < 25:

            insights.append({
                "type": "application",
                "priority": "medium",
                "title": "Keep improving your applications",
                "message": (
                    f"Your interview rate is {interview_rate}%. "
                    "Keep applying consistently while improving "
                    "your application quality."
                )
            })

        else:

            insights.append({
                "type": "application",
                "priority": "low",
                "title": "Strong interview pipeline",
                "message": (
                    f"Your interview rate is {interview_rate}%. "
                    "Your current application strategy is showing "
                    "promising results."
                )
            })

        if offer_applications:

            insights.append({
                "type": "application",
                "priority": "low",
                "title": "Offer received",
                "message": (
                    f"You currently have {len(offer_applications)} "
                    "application(s) marked as an offer."
                )
            })


    # ============================================================
    # GOAL INSIGHTS
    # ============================================================

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

    if goal_count == 0:

        insights.append({
            "type": "goal",
            "priority": "high",
            "title": "Set a career goal",
            "message": (
                "Create a measurable career goal so you can "
                "track your progress."
            )
        })

    elif active_goals:

        average_progress = round(
            sum(
                goal.progress
                for goal in active_goals
            ) / len(active_goals),
            1
        )

        if average_progress < 40:

            insights.append({
                "type": "goal",
                "priority": "high",
                "title": "Focus on your goals",
                "message": (
                    f"Your active goals are currently at "
                    f"{average_progress}% average progress. "
                    "Consider breaking them into smaller milestones."
                )
            })

        elif average_progress < 75:

            insights.append({
                "type": "goal",
                "priority": "medium",
                "title": "Keep pushing your goals",
                "message": (
                    f"Your active goals are at {average_progress}% "
                    "average progress. You're making progress—"
                    "keep the momentum going."
                )
            })

        else:

            insights.append({
                "type": "goal",
                "priority": "low",
                "title": "Goals are nearly there",
                "message": (
                    f"Your active goals are at {average_progress}% "
                    "average progress. Focus on finishing them."
                )
            })

    elif completed_goals:

        insights.append({
            "type": "goal",
            "priority": "low",
            "title": "Set your next challenge",
            "message": (
                "You've completed your current goals. "
                "Create a new challenge to keep progressing."
            )
        })


    # ============================================================
    # LEARNING INSIGHTS
    # ============================================================

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

    if learning_count == 0:

        insights.append({
            "type": "learning",
            "priority": "high",
            "title": "Start a learning path",
            "message": (
                "Add a course, technology or learning resource "
                "to start tracking your development."
            )
        })

    elif active_learning:

        average_learning_progress = round(
            sum(
                item.progress
                for item in active_learning
            ) / len(active_learning),
            1
        )

        if average_learning_progress < 30:

            insights.append({
                "type": "learning",
                "priority": "high",
                "title": "Increase learning consistency",
                "message": (
                    f"Your active learning progress is "
                    f"{average_learning_progress}%. "
                    "Try setting smaller weekly learning targets."
                )
            })

        elif average_learning_progress < 70:

            insights.append({
                "type": "learning",
                "priority": "medium",
                "title": "Keep learning consistently",
                "message": (
                    f"Your active learning progress is "
                    f"{average_learning_progress}%. "
                    "You're moving forward—keep going."
                )
            })

        else:

            insights.append({
                "type": "learning",
                "priority": "low",
                "title": "Finish your learning path",
                "message": (
                    f"Your active learning progress is "
                    f"{average_learning_progress}%. "
                    "You're close to completing it."
                )
            })

    elif completed_learning:

        insights.append({
            "type": "learning",
            "priority": "low",
            "title": "Choose your next skill",
            "message": (
                "You've completed your current learning items. "
                "Consider starting a new technology or advanced topic."
            )
        })


    # ============================================================
    # DEADLINE INSIGHTS
    # ============================================================

    today = date.today()

    upcoming_goals = [
        goal
        for goal in goals
        if goal.target_date
        and goal.target_date >= today
        and (
            not goal.status
            or goal.status.lower() != "completed"
        )
    ]

    if upcoming_goals:

        nearest_goal = min(
            upcoming_goals,
            key=lambda goal: goal.target_date
        )

        days_remaining = (
            nearest_goal.target_date - today
        ).days

        if days_remaining <= 7:

            insights.append({
                "type": "deadline",
                "priority": "high",
                "title": "Goal deadline approaching",
                "message": (
                    f"'{nearest_goal.title}' is due in "
                    f"{days_remaining} day(s). Prioritize it."
                )
            })

        elif days_remaining <= 30:

            insights.append({
                "type": "deadline",
                "priority": "medium",
                "title": "Upcoming goal deadline",
                "message": (
                    f"'{nearest_goal.title}' is due in "
                    f"{days_remaining} days. Keep making progress."
                )
            })


    # ============================================================
    # PRIORITY ORDER
    # ============================================================

    priority_order = {
        "high": 0,
        "medium": 1,
        "low": 2
    }

    insights.sort(
        key=lambda insight: priority_order.get(
            insight["priority"],
            3
        )
    )

    return insights