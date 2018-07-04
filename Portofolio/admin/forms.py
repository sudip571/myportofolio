
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError 
from wtforms.validators import DataRequired, Email, EqualTo


class LoginForm(FlaskForm):

    username=StringField('User Name', validators=[DataRequired('user name is required')])
    password = PasswordField('password',validators=[DataRequired('password is required')])
    submit = SubmitField('Login')