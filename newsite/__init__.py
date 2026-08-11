from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__,template_folder='templates',static_folder='../static')

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///comunidade.db'
app.config['SECRET_KEY'] = '939fd71ece4a2706684d78e864a3ef'

app.config['UPLOAD_FOLDER'] = os.path.join( app.root_path,'..','static','fotos_posts')
   

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'homepage'

from newsite import routes