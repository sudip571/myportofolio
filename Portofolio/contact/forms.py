
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,ValidationError
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):

    email_subject=StringField('Subject',validators=[DataRequired('subject is required')])
    email=StringField('Your Email',validators=[DataRequired('Please write your Email address'),Email('Invalid Email')])
    email_body=TextAreaField('Message',validators=[DataRequired('Please write your message')])
    submit=SubmitField('Send')