"""
The flask application package.
"""
# Third Party Imports
from flask import Flask, redirect, session, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_login  import LoginManager, current_user
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap
from flask_uploads import UploadSet, IMAGES, configure_uploads
from flask_mail import Mail
from datetime import timedelta

# Local Imports
from config import app_config

# Database varaible initialization
app = Flask(__name__,instance_relative_config=True)

# registration for Mail sending
mail = Mail(app)

db=SQLAlchemy()
login_manager = LoginManager()
  
# Application Initialization
def create_app(config_name):
    #app = Flask(__name__,instance_relative_config=True)    
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')

    db.init_app(app)

    #Login Manager comes to play when we have to check if user is logged in before accessing resources
    login_manager.init_app(app)
    login_manager.login_message = "You should be logged in to access this page"
    login_manager.login_view = "admin.login"
    
    # initialize migration
    migrate = Migrate(app,db)
    Bootstrap(app)

    # Configure the image uploading via Flask-Uploads
    configure_image_upload(app)

    # import models in order to create database table
    from Portofolio import models

    #import and register blueprints
    from .admin import admin as admin_blueprint
    from .contact import contac as contact_blueprint
    from .skill import skilll as skill_blueprint
    from .home import home as home_blueprint
    from .aboutt import aboutt as about_blueprint
    from .porto import porto as porto_blueprint

    app.register_blueprint(home_blueprint)
    app.register_blueprint(admin_blueprint)
    app.register_blueprint(contact_blueprint)
    app.register_blueprint(skill_blueprint)
    app.register_blueprint(about_blueprint)
    app.register_blueprint(porto_blueprint)

    return app


def configure_image_upload(app):
    images = UploadSet('images', IMAGES)
    configure_uploads(app, images)


#@app.before_request
#def before_request():
#    print("hey sudip " + request.path)
#    if request.path != '/':
#        session.permanent = True
#        app.permanent_session_lifetime = timedelta(minutes=30)
#        session.modified = True

#        if not (current_user.is_authenticated ) and (request.path != '/login'):
#            return redirect(url_for('admin.login',next=request.endpoint))
        
       
    
        