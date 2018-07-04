

from flask_login import  UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from Portofolio import db,login_manager

class user(UserMixin, db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60),index=True, unique=True)
    password_hash=db.Column(db.String(128))
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    address=db.Column(db.String(50))
    mobile_no=db.Column(db.String(50))
    about_me=db.Column(db.String(800))
    is_admin = db.Column(db.Boolean, default=False)
    email= db.Column(db.String(50),index=True,unique=True)
    @property
    def password(self):
        raise AttributeError('Password is not readable attribute')

    @password.setter
    def password(self,password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.password_hash,password)

    def __repr__(self):
        return '<user:{}>'.format(self.username)

    # Set up user_loader
    @login_manager.user_loader
    def load_user(user_id):
        return user.query.get(int(user_id))




class portofolio(db.Model):

    __tablename__= 'portofolios'

    id = db.Column(db.Integer,primary_key=True)
    project_title=db.Column(db.String(120))
    project_description=db.Column(db.String(1000))
    project_image_path=db.Column(db.String(200))
    technology_used=db.Column(db.String(500))

    def __repr__(self):
        return '<portofolio:{}'.format(self.project_title)

class contact(db.Model):

    __tablename__ = 'contacts'

    id= db.Column(db.Integer,primary_key=True)
    email_subject=db.Column(db.String(50))
    email=db.Column(db.String(60),index=True, unique=True)
    email_body=db.Column(db.String(500))

    def __repr__(self):
        return '<contact:{}'.format(self.email_subject)

class skill(db.Model):
    __tablename__='skills'

    id=db.Column(db.Integer,primary_key=True)
    skill_name=db.Column(db.String(100))
    skillcategory_id=db.Column(db.Integer ,db.ForeignKey('skillcategories.id'))
    


    def __repr__(self):
        return '<skill:{}'.format(self.skill_name)

class skillCategory(db.Model):
    __tablename__='skillcategories'

    id=db.Column(db.Integer,primary_key=True)
    category_name=db.Column(db.String(100))    
    skills =db.relationship('skill',backref='skillcategory',lazy='dynamic')
    def __repr__(self):
        return '<skill:{}'.format(self.category_name)


class company(db.Model):
    __tablename__='companies'
    id=db.Column(db.Integer,primary_key=True)
    company_name=db.Column(db.String(50))
    company_address=db.Column(db.String(50))
    start_date=db.Column(db.String(50))
    end_date=db.Column(db.String(50))

    def __repr__(self):
        return '<skill:{}'.format(self.company_name)

class about(db.Model):
    __tablename__='abouts'
    id=db.Column(db.Integer,primary_key=True)
    first_name=db.Column(db.String(50))
    last_name=db.Column(db.String(50))
    address=db.Column(db.String(50))
    mobileno=db.Column(db.String(50))
    email=db.Column(db.String(50),index=True,unique=True)
    about_me=db.Column(db.String(1000))

    def __repr__(self):
        return '<about:{}'.format(self.first_name)