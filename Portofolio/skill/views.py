from flask_login import login_required
from flask import flash, render_template, redirect, url_for, abort

from . import skilll
from .. import db
from .forms import SkillCategoryForm, SkillForm
from ..models import skillCategory,skill 


@skilll.route('/skillcategory',methods=['GET','POST'])
@login_required
def list_skill_category():
    skillcategory=skillCategory.query.all()
    return render_template('admin/skill_categories.html',skillCategory=skillcategory)

@skilll.route('/skillcategory/add',methods=['GET','POST'])
@login_required
def add_skill_category():

    add_skillcategory=True
    form = SkillCategoryForm()
    if form.validate_on_submit():
        skill_category=skillCategory(
            category_name=form.category.data
            )
        try:
            db.session.add(skill_category)
            db.session.commit()
            flash('New skill category has been added')
        except Exception as e:
            flash(str(e))
        return redirect(url_for('skill.list_skill_category'))

    return render_template('admin/skill_category.html',form=form,action="Add",add_skillcategory=add_skillcategory)

@skilll.route('/skillcategory/edit/<int:id>',methods=['GET','POST'])
@login_required
def edit_skill_category(id):
    add_skillcategory=False
    skill_category=skillCategory.query.get_or_404(id)
    form=SkillCategoryForm(obj = skill_category)
    if form.validate_on_submit():
        skill_category.category_name=form.category.data
        db.session.commit()
        flash("skill category has been Edited")
        return redirect(url_for('skill.list_skill_category'))

    #form.category.data=skill_category.category_name
    return render_template('admin/skill_category.html',form=form,action="Edit",add_skillcategory=add_skillcategory)

@skilll.route('/skillcategory/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete_skill_category(id):

    skill_category=skillCategory.query.get_or_404(id)
    db.session.delete(skill_category)
    db.session.commit()
    flash('data has been deleted')
    return redirect(url_for('skill.list_skill_category'))


# Skill View
@skilll.route('/skills')
@login_required
def list_skill():
    result=skill.query.all()
    return render_template('admin/skills.html',skills=result)



@skilll.route('/skill/add',methods=['GET','POST'])
@login_required
def add_skill():
    add_skill=True
    form= SkillForm()
    if form.validate_on_submit():
        skill_value=skill()
        skill_value.skill_name=form.skill_name.data
        skill_value.skillcategory=form.skillcategory.data
        db.session.add(skill_value)
        db.session.commit()
        flash('Skill has been added')
        
        return redirect(url_for('skill.list_skill'))


    return render_template('admin/skill.html',add_skill=add_skill,form=form,action="Add")

@skilll.route('/skill/edit/<int:id>',methods=['GET','POST'])
@login_required
def edit_skill(id):
    add_skill=False
    result=skill.query.get_or_404(id)
    form= SkillForm(obj=result)
    if form.validate_on_submit():
        
        result.skill_name=form.skill_name.data
        result.skillcategory=form.skillcategory.data
        #db.session.add(skill_value)
        db.session.commit()
        flash('Skill has been Edited')
        
        return redirect(url_for('skill.list_skill'))


    return render_template('admin/skill.html',add_skill=add_skill,form=form,action="Edit")

@skilll.route('/skill/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete_skill(id):

    result=skill.query.get_or_404(id)
    db.session.delete(result)
    db.session.commit()
    flash('data has been deleted')
    return redirect(url_for('skill.list_skill'))