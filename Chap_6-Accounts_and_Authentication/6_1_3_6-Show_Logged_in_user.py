# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 3. Introduction to Authentication with Flask
# 6. Show Logged in user

'''
In the previous exercise, we were able to write the login code. Now in this 
section, we will show the information related to the logged-in user.

Let's zoom into this code: Notice how we pass in user into the current_user
object. We will be using that current_user object in our HTML.


  user = User(email="TheCodeLearner@gmail.com", usernmae="TheCodeLearner", password="!aehashf0qr324*&#W)*E!")
  login_user(user)
  return render_template('logged_in.html', current_user=user)
return 'Bad login'


Now when a user logs in successfully they are sent to a page showing our 
logged_in info. Most likely in our application, we will be serving dynamic
pages of HTML. We can use Jinja templates to render the data from the backend.
To display the user, pass it in from the endpoint and access that variable
in our HTML.


<h1>Welcome to Our Home Page</h1>
<p>Welcome {{ current_user.username }}</p>
<a class="blue pull-left" href="{{ url_for('index')" }}>back</a>


This will enable our users to see their data when they log in!

'''

# see the .html


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
    login_user(user)
    return render_template("logged_in.html", current_user=user )
  return login_manager.unauthorized()

@app.route('/home')
@login_required
def home():
	return render_template('logged_in.html')

@login_manager.unauthorized_handler
def unauthorized():
    # do stuff
    return "You are not logged in. Click here to get <a href="+ str("/")+">back to Landing Page</a>"