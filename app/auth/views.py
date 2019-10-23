from . import auth
from flask import render_template,redirect,url_for,flash,request
from .. import db,mail
from .forms import RegistrationForm,LoginForm
from ..models import User
from flask_login import login_user,logout_user,login_required
from flask_mail import Message


@auth.route('/login',methods = ["GET","POST"])
def login():
  login_form = LoginForm()
  if login_form.validate_on_submit():
    user = User.query.filter_by(email = login_form.email.data).first()
    if user is not None and user.verify_password(login_form.password.data):
      login_user(user,login_form.remember_me.data)
      try:
        msg = Message('Hello...Welcome to pitches',sender='denismugendinjue9@gmail.com')
        msg.add_recipient(user.email)
        mail.send(msg)
      except Exception as e:
        print('failed')
      return redirect(request.args.get('next') or url_for('main.home'))
    flash('invalid user')
  return render_template('login.html',loginF = login_form)

@auth.route('/signup',methods = ["GET","POST"])
def signup():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(email = form.email.data,username = form.username.data,password = form.password.data)
    user.save()
    return redirect(url_for('auth.login'))
  return render_template('signup.html',regi_form = form)

@auth.route('/logout')
@login_required
def logout():
  logout_user()
  return redirect(url_for('main.index'))