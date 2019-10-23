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


