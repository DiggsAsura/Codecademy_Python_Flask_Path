# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 3. Introduction to Authentication with Flask
# 3. Protecting Pages

'''
Protecting pages is the primary objective of authentication. We can leverage some
very useful functions from Flask-Login to ensure our different pages or routes
are protected.

One of the key pieces of code that we previously added is the LoginManager object
that we initialized with our instance of the Flask application. LoginManagers
have a method user_loader that needs to be defined in order to load and verify
a user from our database.


@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))


- this method retrieves our User with an id value id from our database

- without this function, we won't be able to verify users on our protected
  routes!

Next we need to import the loagin_required function from flask_login at the top
of our file:


from flask_login import login_required


We can now add the @login_required function as a decorator to different routes
to make logging in necessary.


@app.route('/home')
@login_required
def home():
  return render_template('logged_in.html')


The @login_required decorator will force the user to login before being able 
to view the page
'''

import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required
from flask import request, render_template, flash, redirect, url_for
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

app = flask.Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  posts = db.relationship('Post', backref='author', lazy='dynamic')

  def __repr__(self):
    return f'<User {self.username}'

  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
  
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

@login_manager.user_loader
def load_user(id):
  return User.query.get(int(id))

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/home')
@login_required
def home():
  return render_template('logged_in.html')