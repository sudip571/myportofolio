
from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField, SubmitField, ValidationError
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileRequired, FileAllowed
from flask_uploads import UploadSet, IMAGES


images=UploadSet('images',IMAGES)

class PortoForm(FlaskForm):

    project_title=StringField('Project Title',validators=[DataRequired()])
    project_description=TextAreaField('Project Description')
    technology_used=TextAreaField('Technology Used')
    project_image_upload=FileField('Upload Image',validators=[FileAllowed(images,"Upload Image only")])
    submit=SubmitField('Submit')