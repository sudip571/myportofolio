from flask import render_template, redirect, url_for, flash, session, app, request
from flask_login import login_required, login_user, logout_user
from datetime import timedelta

from . import admin
from .forms import LoginForm
from .. import db
from ..models import user


@admin.route('/dashboard')
@login_required
def dashboard():
    return render_template('admin/dashboard.html',title='Dashboard')

@admin.route('/login',methods=['GET','POST'])
def login():

    form = LoginForm()
    if form.validate_on_submit():
        result=user.query.filter_by(username=form.username.data).first()
        if result is not None and result.verify_password(form.password.data):
            login_user(result)                    

            next_url=request.values.get('next')
            if next_url is None:
                return redirect(url_for('admin.dashboard'))                
            else:                
                return redirect(next_url)                            
        else:
            flash('Invalid username or password')

    return render_template('admin/login.html',form=form,title='Login',myname="sudip")

@admin.route('/logout')

def logout():
    logout_user()
    #flash('you have successfully been logged out')
    return redirect(url_for('home.homepage'))


#another way of redirecting 
 #next = flask.request.args.get('next')
 #       # is_safe_url should check if the url is safe for redirects.
 #       # See http://flask.pocoo.org/snippets/62/ for an example.
 #       if not is_safe_url(next):
 #           return flask.abort(400)

 #       return flask.redirect(next or flask.url_for('index'))