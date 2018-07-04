from flask_login import login_required
from flask import flash,render_template,redirect, abort, url_for

from . import aboutt
from .forms import AboutForm
from .. import db
from ..models import about


@aboutt.route('/info',methods=['GET','POST'])
@login_required
def info():
    result= about.query.all()
    return render_template('admin/inform.html',aboutme=result)

@aboutt.route('/info/add',methods=['GET','POST'])
@login_required
def add_info():
    add_information=True
    form=AboutForm()
    if form.validate_on_submit():
        new_info=about()
        new_info.about_me=form.about_me.data
        new_info.address=form.address.data
        new_info.email=form.email.data
        new_info.first_name=form.first_name.data
        new_info.last_name=form.last_name.data
        new_info.mobileno=form.mobileno.data
        
        db.session.add(new_info)
        db.session.commit()
        flash('Info has been added')
        return redirect(url_for('aboutt.info'))
    return render_template('admin/info.html',form=form,add_information=add_information,action="Add" )

@aboutt.route('/info/edit/<int:id>',methods=['GET','POST'])
@login_required
def edit_info(id):
    add_information=False
    result=about.query.get_or_404(id)
    form=AboutForm(obj=result)
    if form.validate_on_submit():
        
        result.about_me=form.about_me.data
        result.address=form.address.data
        result.email=form.email.data
        result.first_name=form.first_name.data
        result.last_name=form.last_name.data
        result.mobileno=form.mobileno.data       
        
        db.session.commit()
        flash('Info has been updated')
        return redirect(url_for('aboutt.info'))
    return render_template('admin/info.html',form=form,add_information=add_information,action="Edit" )

@aboutt.route('/info/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete_info(id):
    result=about.query.get_or_404(id)
    db.session.delete(result)
    db.session.commit()
    flash('Info has been deleted')
    return redirect(url_for('aboutt.info'))
    
   
            
            
            
