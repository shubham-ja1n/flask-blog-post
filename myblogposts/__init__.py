from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os

app = Flask(__name__)

app.config['SECRET_KEY'] = "mysecretkey"

########################  DATABASE SETUP  ###########################
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{basedir}/data.sqlite"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app, db)
#####################################################################

#######################  LOGIN CONFIGURATIONS  #####################
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'users.login'
#####################################################################


from myblogposts.core.views import core
from myblogposts.error_pages.handlers import error_page
from myblogposts.users.views import users
from myblogposts.blog_posts.views import blog_posts

app.register_blueprint(core)
app.register_blueprint(error_page)
app.register_blueprint(users)
app.register_blueprint(blog_posts)