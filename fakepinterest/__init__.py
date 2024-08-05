import sqlalchemy
# pip install (flask, flask-alchemy, flask-login, flask-bcrypt)
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
import os

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///comunidade.db"
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config["SECRET_KEY"] = "b978ebba5c957c34a6c5ffdb6c537c86"
app.config['UPLOAD_FOLDER'] = "static/fotos_posts"

database = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

#confifuracoes de login (se o usuario nao estiver logado, para onde ele sera redirecionado)
login_manager.login_view = "homepage"

from fakepinterest import routes
