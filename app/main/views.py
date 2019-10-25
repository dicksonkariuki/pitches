from . import main
from flask import redirect,render_template,url_for,request,abort,flash
from flask_login import login_required,current_user
from ..models import User,Pitch,Comments,Upvote,Downvote
from .forms import updateForm,postdata
from .. import db,photos



@main.route('/')
def index():
  return render_template('index.html')

@main.route('/home',methods = ["GET","POST"])
@login_required
def home():
  comment = Comments.query.all()
  pitch = Pitch.query.all()
  form = postdata()
  if form.validate_on_submit():
    posts = Pitch(title = form.title.data,category=form.category.data,the_pitch=form.post.data,pitch=current_user)
    posts.save()
    return redirect(url_for('main.home'))
  return render_template('home.html',form = form,pitch = pitch,comment = comment)

@main.route('/profile/<the_user>')
def profile(the_user):
  pitch = Pitch.query.filter_by(user_id = current_user.id).all()

  user = User.query.filter_by(username = the_user).first()
  if user == None:
    abort(404)

  return render_template('profile.html',user = user, pitch = pitch)

@main.route('/profile/<the_user>/update',methods = ["GET","POST"])
@login_required
def profile_upt(the_user):

  user = User.query.filter_by(username=the_user).first()
  if user == None:
    abort(404)

  upt = updateForm()

  if upt.validate_on_submit():
    user.user_bio = upt.bio.data
    user.save()

    return redirect(url_for('main.profile',the_user = user.username))
  return render_template('updateUser.html',form = upt)

@main.route('/user/<the_user>/update/pic',methods = ["GET","POST"])
@login_required
def update_pic(the_user):
  user = User.query.filter_by(username = the_user).first()
  if 'photo' in request.files:
    filename = photos.save(request.files['photo'])
    path = f'photos/{filename}'
    user.user_profile_pic_path = path
    db.session.commit()
  return redirect(url_for('.profile',the_user=current_user))


@main.route('/post/<int:pitch_id>',methods = ["POST"])
@login_required
def delete(pitch_id):
  delete = Pitch.query.get(pitch_id)
  if delete.pitch != current_user:
    flash('Cannot delete other users pitches')
    return redirect(url_for('main.home')) 
  delete.delete()
  return redirect(url_for('main.home'))


@main.route('/comments/<int:pitch_id>',methods = ["GET","POST"])
@login_required
def commenting(pitch_id):
  comment_post = Comments.query.filter_by(pitch_id = pitch_id)
  if request.method == "POST":
    comment = request.form.get("comment")
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    cmt = Comments(the_comment = comment,author = current_user,pitchcomment = pitch)
    cmt.save()
    return redirect(url_for('main.viewcomments',pitch_id = pitch_id))
  return render_template('main.index')


@main.route('/view/<pitch_id>',methods = ["GET","POST"])
@login_required
def viewcomments(pitch_id):
  pitch = Pitch.query.filter_by(id = pitch_id ).first()
  comment = Comments.query.filter_by(pitch_id = pitch_id).all()
  return render_template('comments.html',comment = comment,pitch = pitch)

@main.route('/upvote/<pitch_id>')
@login_required
def upvote(pitch_id):
  user = current_user
  if user.is_authenticated:
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    upvote = Upvote.query.filter_by(user_id = user.id , pitch_id = pitch.id).first()
    if upvote != None:
      upvote.delete()
      return redirect(url_for('main.home'))
    else:
      downvote = Downvote.query.filter_by(user = user , pitch = pitch).first()
      if downvote != None:
        downvote.delete()
      upvote = Upvote(vote = True , user = user , pitch = pitch)
      upvote.save()
      return redirect(url_for('main.home'))
  return redirect(url_for('main.home'))

@main.route('/downvote/<pitch_id>')
@login_required
def downvote(pitch_id):
  user = current_user
  if user.is_authenticated:
    pitch = Pitch.query.filter_by(id = pitch_id).first()
    downvote = Downvote.query.filter_by(user_id = user.id , pitch_id = pitch.id).first()
    if downvote != None:
      downvote.delete()
      return redirect(url_for('main.home'))
    else:
      upvote = Upvote.query.filter_by(user = user , pitch = pitch).first()
      if upvote != None:
        upvote.delete()
      downvote = Downvote(vote = True , user = user , pitch = pitch)
      downvote.save()
      return redirect(url_for('main.home'))
  return redirect(url_for('main.home'))