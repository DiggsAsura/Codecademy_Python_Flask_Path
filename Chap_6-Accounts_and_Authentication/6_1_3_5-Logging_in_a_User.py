# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 3. Introduction to Authentication with Flask
# 5. Logging in a User

'''
Best practices for user authentication using Flask is to make it hard for 
someone to use a stolen credential.

To achieve this in Flask use the Flask's Werkzeug library which has
generate_password_hash method to generate a hash, and check_password_hash
method to compare login input with the value returned from the 
check_password_hash method.

Our login code will check wheter the value passed in is the same as the hardcoded
user we are using to emulate a database.

We create a User class to represent a user. This object takes advantage of 
UserMixin (Mixins are prepackaged code of common code needs). In this case we use
UserMixin because it allows us to take advantage of common user account functions
without having to write it all ourselves from scratch.

The code below is the logic we use to log a user in if their password is 
correct:


@app.route('/', methods=['GET', 'POST'])
def index():
  if flask.request.method == 'GET':
    return """
    <p>Your credentials:
    username: TheCodeLearner
    password: !aehashf0qr324*&#W)*E!
    </p>
    <form action='/' method='POST'>
      <input type='text' name='email' id='email' placeholder='email'/>
      <input type='password' name='password' id='password' placeholder='password'/>
      <input type='submit' name='submit'/>
    </form>
    """
  email = "TheCodeLearner"
  if flask.request.form['password'] == "!aehashf0qr324*&#W)*E!":
    user = User(email="TheCodeLearner@gmail.com", username="TheCodeLearner", password="!aehashf0qr324*&#W)*E!")
    login_user(user)
    return render_template("logged_in.html", current_user=user)
  return login_manager.unauthorized()
  
  
Take a look at the second conditional:


if flask.request.form['password'] == "!aehashf0qr324*&#W)*E!":


Here, we're checking that the form was submitted with a password that has the
value "!aehashf0qr324*&#W)*E!". If the password matches "!aehashf0qr324*&#W)*E!"
exactly, then we can create a new User instance with the properties specified
above and save the object to user. We then use the login_user(user) to load
the newly created User instance. Once logged in, we can load the proper page 
using render_template('logged_in.html', current_user=user). If the password 
isn't correct, we return login_manager.unauthorized().

'''

import flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_required, login_user
from flask import request, render_template, flash, redirect,url_for
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


app = flask.Flask(__name__)
app.secret_key = 'secretkeyhardcoded'
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)

class User(UserMixin,db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
    
@app.route('/', methods=['GET', 'POST'])
def index():
  if flask.request.method == 'GET':
    return '''
    <p>Your credentials:
    username: TheCodeLearner
    password: !aehashf0qr324*&#W)*E!
    </p>
               <form action='/' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''
  email = "TheCodeLearner"
  if flask.request.form['password'] == "!aehashf0qr324*&#W)*E!":
    user = User(email="TheCodeLearner@gmail.com", username="TheCodeLearner",password="!aehashf0qr324*&#W)*E!")
    # Add your code below:
    login_user(user)
    return render_template('logged_in.html', current_user=user)
  return login_manager.unauthorized()

@app.route('/home')
@login_required
def home():
	return render_template('logged_in.html')

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return "You are not logged in. Click here to get <a href="+ str("/")+">back to Landing Page</a>"
