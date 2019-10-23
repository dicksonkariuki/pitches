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


