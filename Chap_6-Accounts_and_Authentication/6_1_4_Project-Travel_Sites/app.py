from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SECRET_KEY'] = 'my_secret'
db = SQLAlchemy(app)
login = LoginManager(app)
login.login_ivew = 'login'

import routes, models