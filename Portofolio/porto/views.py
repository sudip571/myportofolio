from flask_login import login_required
from flask import flash, redirect, render_template, abort, url_for, current_app
from werkzeug.utils import secure_filename
import os


from .forms import PortoForm
from . import porto
from .. import db
from .. import app
from ..models import portofolio

@porto.route('/portofolio')
@login_required
def portofo():
    result= portofolio.query.all()
    image_folder=app.config['UPLOADS_DEFAULT_DEST']
    return render_template('admin/portofolio.html',myporto=result,image_folder=image_folder)

@porto.route('/portofolio/add',methods=['GET','POST'])
@login_required
def add_portofo():
    add_information=True
    form=PortoForm()
    if form.validate_on_submit():
        
        uploaded_image=form.project_image_upload.data
        filename= secure_filename(uploaded_image.filename)
        uploaded_image.save(os.path.join(app.config['UPLOADS_DEFAULT_DEST'],filename))

        new_info=portofolio()
        new_info.project_title=form.project_title.data
        new_info.project_description=form.project_description.data
        new_info.technology_used=form.technology_used.data
        new_info.project_image_path=filename
      
        
        db.session.add(new_info)
        db.session.commit()
        flash('Portofolio has been added')
        return redirect(url_for('porto.portofo'))
    return render_template('admin/portofolioo.html',form=form,add_information=add_information,action="Add" )

@porto.route('/portofolio/edit/<int:id>',methods=['GET','POST'])
@login_required
def edit_portofo(id):
    add_information=False
    result=portofolio.query.get_or_404(id)
    form=PortoForm(obj=result)
    if form.validate_on_submit():

        uploaded_image=form.project_image_upload.data
        filename= secure_filename(uploaded_image.filename)
        uploaded_image.save(os.path.join(app.config['UPLOADS_DEFAULT_DEST'],filename))
        
        result.project_title=form.project_title.data
        result.project_description=form.project_description.data
        result.technology_used=form.technology_used.data
        result.project_image_path=filename             
        
        db.session.commit()
        flash('Portofolio has been updated')
        return redirect(url_for('porto.portofo'))
    return render_template('admin/portofolioo.html',form=form,add_information=add_information,action="Edit" )

@porto.route('/portofolio/delete/<int:id>',methods=['GET','POST'])
@login_required
def delete_portofo(id):
    result=portofolio.query.get_or_404(id)
    db.session.delete(result)
    db.session.commit()
    flash('Portofolio has been deleted')
    return redirect(url_for('porto.portofo'))
