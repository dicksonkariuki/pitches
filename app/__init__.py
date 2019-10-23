from flask import Flask
from flas_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_moment import Moment

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
photos = UploadSet('photos', IMAGES)
mail = Mail()
moment = Moment()

def create_app(config_name):

    app = Flask(__name__)
# Creating the app configurations.
    app.config.from_object(config_options[config_name])