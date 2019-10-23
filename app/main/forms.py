from . import main
from flask_wtf import FlaskForm
from wtforms import SubmitField,TextAreaField,StringField
from wtforms.validators import Required


class updateForm(FlaskForm):
  bio = TextAreaField('Enter your bio',validators=[Required()])
  submit = SubmitField('submit')

class postdata(FlaskForm):
  category = StringField('Enter a catogory', validators=[Required()])
  title = StringField('Enter your title', validators=[Required()])
  post = TextAreaField('Enter your 1 min pitch', validators=[Required()])
  submit = SubmitField('submit')