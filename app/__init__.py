from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db, compare_type=True)
login = LoginManager(app)
login.login_view = 'signin'

from app import routes
