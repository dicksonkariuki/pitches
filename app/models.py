from . import db,login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime


class User(UserMixin,db.Model):
  __tablename__="users"
  id = db.Column(db.Integer,primary_key=True)
  username = db.Column(db.String(255),unique = True,nullable = False)
  email = db.Column(db.String(255),unique = True,nullable = False)
  passW = db.Column(db.String(255),nullable = False)
  pitch = db.relationship('Pitch',backref = 'pitch',lazy="dynamic")
  comment = db.relationship('Comments',backref = 'author',lazy="dynamic")
  user_bio = db.Column(db.String(255))
  user_profile_pic_path = db.Column(db.String())
  upvote = db.relationship('Upvote',backref = 'user',lazy = 'dynamic')
  downvote = db.relationship('Downvote',backref = 'user',lazy = 'dynamic')

  @property
  def password(self):
    raise AttributeError('You cannot read the password')

  @password.setter
  def password(self,password):
    self.passW = generate_password_hash(password)

  def verify_password(self,password):
    return check_password_hash(self.passW,password)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  @login_manager.user_loader
  def user_loader(user_id):
    return User.query.get(user_id)
    
  def __repr__(self):
    return f'User {self.username}'




class Pitch(db.Model):
  __tablename__="pitch"
  id = db.Column(db.Integer,primary_key=True)
  the_pitch = db.Column(db.String(255),nullable = False)
  category = db.Column(db.String(255),nullable = False)
  title = db.Column(db.String(255),nullable = False)
  date_posted = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=False)
  comment = db.relationship('Comments',backref = 'pitchcomment',lazy="dynamic")
  upvote = db.relationship('Upvote',backref = 'pitch',lazy = 'dynamic')
  downvote = db.relationship('Downvote',backref = 'pitch',lazy = 'dynamic')

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return f'User {self.the_pitch}'

class Comments(db.Model):
  __tablename__="comment"
  id = db.Column(db.Integer,primary_key=True)
  the_comment = db.Column(db.String(255),nullable = False)
  date_posted = db.Column(db.DateTime,nullable = False,default = datetime.utcnow)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=True)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'),nullable=True)
  

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def __repr__(self):
    return f'User {self.the_comment}'

class Upvote(db.Model):
  __tablename__="upvote"
  id = db.Column(db.Integer,primary_key=True)
  vote = db.Column(db.String(10),nullable = False)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=True)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'),nullable=True)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

class Downvote(db.Model):
  __tablename__="downvote"
  id = db.Column(db.Integer,primary_key=True)
  vote = db.Column(db.String(10),nullable = False)
  user_id = db.Column(db.Integer,db.ForeignKey('users.id'),nullable=True)
  pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'),nullable=True)

  def save(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()