from flask_login import login_required
from flask import render_template, redirect,url_for, flash
import json


from . import contac
from .. import db,app
from ..models import contact 
from .forms import ContactForm
from .send_email import send_emails

@contac.route('/emails')
@login_required
def get_email():
    result=contact.query.all()
    return render_template('admin/contact.html',emails=result)

@contac.route('/send_message',methods=['POST'])
@login_required
def add_email():
    form=ContactForm()    
    if form.validate_on_submit():
        try:
            contact_data=contact()
            contact_data.email=form.email.data
            contact_data.email_body=form.email_body.data
            contact_data.email_subject=form.email_subject.data

            db.session.add(contact_data)
            db.session.commit()

            send_emails(form.email_subject.data,app.config['MAIL_DEFAULT_SENDER'],app.config['EMAIL_RECEIVER'],render_template("admin/email_body.txt",message_sender_email=form.email.data,message=form.email_body.data),render_template("admin/email_body.html",message_sender_email=form.email.data,message=form.email_body.data))

            status_dic={'status':'success','message':'Your message has been sent'}
            return json.dumps(status_dic)
        except Exception as e:
            db.session.rollback()
            raise e
        

        
    return get_error(form)

      

@contac.route('/emails/delete/<int:id>')
@login_required
def delete_email(id):
    result=contact.query.get_or_404(id)
    db.session.delete(result)
    db.session.commit()
    flash('email has been deleted')
    return redirect(url_for('contact.get_email'))



def get_error(form):
    error_list={'status':'failure'}
    for field, errors in form.errors.items():
        for error in errors:         
           error_list['message']= error
    return json.dumps(error_list)


#dictionary_obj={'x':1,'y':2}
#to loop over keys only--> for key_item in dictionary_obj:
#to loop over both key and value --> for key_item,value_item in dictionary_obj.items():
#to loop further over key_item/value_item --> for item in key_item/value_item:
#def flash_errors(form):
#    for field, errors in form.errors.items():
#        for error in errors:
#            flash(u"Error in the %s field - %s" % (
#                getattr(form, field).label.text,
#                error
#            ))

