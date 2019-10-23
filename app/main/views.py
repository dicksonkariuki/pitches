from flask import render_template,redirect,url_for,flash,request,abort 
from . import main 
from flask_login login_required,current_user
from .forms import UpdateProfile,PitchForm,CommentForm
from ..import db,photos
from ..models import User,PitchCategory,Pitches,Comments

@main.route('/')
def index():
    """View root page function that returns index page and the various news sources"""

    title = 'Home- Welcome to the Pitch Website'
    categories = PitchCategory.get_categories()
    return render_template('index.html', title=title, categories=categories)

@main.route('/category/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    '''
    Function to check Pitches form
    '''
    form = PitchForm()
    category = PitchCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        actual_pitch = form.content.data
        new_pitch = Pitches(actual_pitch=actual_pitch,
                            user_id=current_user.id, category_id=category.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id=category.id))

    return render_template('new_pitch.html', pitch_form=form, category=category)
# Routes for displaying the different pitches


@main.route('/category/<int:id>')
def category(id):
    '''
    category route function returns a list of pitches in the category chosen
    '''

    category = PitchCategory.query.get(id)

    if category is None:
        abort(404)

    pitches = Pitches.get_pitches(id)
    return render_template('category.html', category=category, pitches=pitches)

@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def single_pitch(id):
    '''
    Function the returns a single pitch for comment to be added
    '''

    pitches = Pitches.query.get(id)

    if pitches is None:
        abort(404)

    comment = Comments.get_comments(id)
    return render_template('pitch.html', pitches=pitches, comment=comment)

# Routes for user authentication
@main.route('/user/<uname>')
@login_required
def profile(uname):
    user = User.query.filter_by(username=uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user=user)


