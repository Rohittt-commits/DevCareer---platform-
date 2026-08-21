from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models.skill import Skill


skills = Blueprint("skills", __name__, url_prefix="/skills")


@skills.route("/")
@login_required
def list_skills():
    user_skills = Skill.query.filter_by(
        user_id=current_user.id
    ).order_by(Skill.created_at.desc()).all()

    return render_template(
        "skills/list.html",
        skills=user_skills
    )


@skills.route("/add", methods=["GET", "POST"])
@login_required
def add_skill():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        proficiency = request.form.get("proficiency", type=int)
        experience_months = request.form.get(
            "experience_months",
            type=int
        )
        notes = request.form.get("notes", "").strip()

        if not name:
            flash("Skill name is required.", "danger")
            return redirect(url_for("skills.add_skill"))

        if not proficiency or not 1 <= proficiency <= 5:
            flash("Proficiency must be between 1 and 5.", "danger")
            return redirect(url_for("skills.add_skill"))

        if experience_months is None or experience_months < 0:
            flash("Experience cannot be negative.", "danger")
            return redirect(url_for("skills.add_skill"))

        skill = Skill(
            user_id=current_user.id,
            name=name,
            category=category or None,
            proficiency=proficiency,
            experience_months=experience_months,
            notes=notes or None
        )

        db.session.add(skill)
        db.session.commit()

        flash("Skill added successfully!", "success")
        return redirect(url_for("skills.list_skills"))

    return render_template("skills/add.html")


@skills.route("/<int:skill_id>/edit", methods=["GET", "POST"])
@login_required
def edit_skill(skill_id):
    skill = Skill.query.filter_by(
        id=skill_id,
        user_id=current_user.id
    ).first_or_404()

    if request.method == "POST":
        name = request.form.get("name", "").strip()
        category = request.form.get("category", "").strip()
        proficiency = request.form.get("proficiency", type=int)
        experience_months = request.form.get(
            "experience_months",
            type=int
        )
        notes = request.form.get("notes", "").strip()

        if not name:
            flash("Skill name is required.", "danger")
            return redirect(
                url_for("skills.edit_skill", skill_id=skill.id)
            )

        if not proficiency or not 1 <= proficiency <= 5:
            flash("Proficiency must be between 1 and 5.", "danger")
            return redirect(
                url_for("skills.edit_skill", skill_id=skill.id)
            )

        if experience_months is None or experience_months < 0:
            flash("Experience cannot be negative.", "danger")
            return redirect(
                url_for("skills.edit_skill", skill_id=skill.id)
            )

        skill.name = name
        skill.category = category or None
        skill.proficiency = proficiency
        skill.experience_months = experience_months
        skill.notes = notes or None

        db.session.commit()

        flash("Skill updated successfully!", "success")
        return redirect(url_for("skills.list_skills"))

    return render_template(
        "skills/edit.html",
        skill=skill
    )


@skills.route("/<int:skill_id>/delete", methods=["POST"])
@login_required
def delete_skill(skill_id):
    skill = Skill.query.filter_by(
        id=skill_id,
        user_id=current_user.id
    ).first_or_404()

    db.session.delete(skill)
    db.session.commit()

    flash("Skill deleted successfully!", "success")
    return redirect(url_for("skills.list_skills"))