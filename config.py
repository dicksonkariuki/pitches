import os
from dotenv import load_dotenv
load_dotenv()


class Config:
  """
  configuration classes
  """

  # SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:kariuki@localhost/pitch'
  UPLOADS_DEFAULT_DEST = 'app/static/photos/photos'
  MAIL_SERVER = 'smtp.gmail.com'
  MAIL_PORT = 465
  MAIL_USE_TLS = False
  MAIL_USE_SSL = True
  MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
  MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
  SECRET_KEY = os.urandom(32)

class Development(Config):
  """
  development
  """
  DEBUG=True

class Production(Config):
  """
  production
  """
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

configurations = {
                 "Development":Development,
                 "Production":Production
                  }