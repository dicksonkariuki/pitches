from flask_wtf import FlaskForm 
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError
from wtforms import StringField,PasswordField,BooleanField,SubmitField
