from flask import Flask
from config import configurations
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import configure_uploads,UploadSet,IMAGES
from flask_mail import Mail

login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.login'

bootstrap = Bootstrap()
db = SQLAlchemy() 
photos = UploadSet('photos',IMAGES)
mail = Mail()




def create_app(config_name):
  app = Flask(__name__)

  app.config.from_object(configurations[config_name])


  login_manager.init_app(app)
  configure_uploads(app,photos)
  mail.init_app(app)
  db.init_app(app)
  bootstrap.init_app(app)

  from .auth import auth as auth_blueprint
  app.register_blueprint(auth_blueprint)

  from .main import main as main_blueprint
  app.register_blueprint(main_blueprint)  

  return app

