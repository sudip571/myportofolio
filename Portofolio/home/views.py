
from flask import redirect, render_template, flash, url_for
from Portofolio.contact.forms import ContactForm

from . import home
from .. import  db
from ..models import user,portofolio,contact,skill,skillCategory,company,about



@home.route('/')
def homepage():
    form=  ContactForm()
    about_section= about.query.first()
    skill_section = skill.query.all()
    work_section = company.query.all()
    porto_section = portofolio.query.all()

    return render_template('home.html',title='Welcome',form=form,about_section=about_section,skill_section=skill_section,work_section=work_section,porto_section=porto_section)