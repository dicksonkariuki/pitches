from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,TextAreaField
from wtforms.validators import Required,Email,EqualTo
from ..models import User
from wtforms import ValidationError

class RegistrationForm(FlaskForm):
  email = StringField('Enter Email Addess: ',validators=[Required(),Email()])
  username = StringField('Enter your username: ',validators=[Required()])
  password = PasswordField('Enter a password: ',validators=[Required(),EqualTo('password_confirm',message='passwords must match')])
  password_confirm = PasswordField('Confirm your password',validators=[Required()])
  Submit = SubmitField ('sign up')

  def validate_email(self,data_field):
    if User.query.filter_by(email = data_field.data).first():
      raise ValidationError('There is an account with that Email')

  def validate_username(self,data_field):
    if User.query.filter_by(username = data_field.data).first():
      raise ValidationError('Username already taken')

class LoginForm(FlaskForm):
  email = StringField('Enter your Email:',validators=[Required(),Email()])
  password = PasswordField('Enter your password:',validators=[Required()])
  remember_me =BooleanField('remember_me')
  submit = SubmitField('log in')