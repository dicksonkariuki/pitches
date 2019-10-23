from flask import flask
from flask_sqlalchemy import SQLAlchemy
bootstrap = Bootstrap()
db = SQLAlchemy()
app = Flask(__name__)