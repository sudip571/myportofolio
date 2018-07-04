
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Email

class AboutForm(FlaskForm):
    first_name=StringField('FirstName',validators=[DataRequired()])
    last_name=StringField('LastName',validators=[DataRequired()])
    address=StringField('Address',validators=[DataRequired()])
    about_me=TextAreaField('My Description',validators=[DataRequired()])
    email=StringField('Email',validators=[DataRequired(),Email()])
    mobileno=StringField('Mobile No')
    submit=SubmitField('Submit')

