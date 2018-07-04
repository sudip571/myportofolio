
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, ValidationError
from wtforms.validators import DataRequired
from wtforms.ext.sqlalchemy.fields import QuerySelectField


from ..models import skillCategory

class SkillCategoryForm(FlaskForm):
    category= StringField('Skill Category',validators=[DataRequired('Category Name is required')])
    submit=SubmitField('Submit')

class SkillForm(FlaskForm):
    skillcategory=QuerySelectField(query_factory=lambda: skillCategory.query.all(), get_label="category_name")
    skill_name=StringField("Skill",validators=[DataRequired(" Skill is required")])
    submit=SubmitField("submit")