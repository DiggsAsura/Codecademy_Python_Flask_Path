# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 2. Introduction to Accounts
# 5. Login in with Flask

'''
We currently have a working form grabbing user data and signing them up to our
application. Good work! Next, let's allow users to login by using a Flask-Login
object called LoginManager().


login_manager = LoginManager()
login_manager.init_app(app)


- here we create a LoginManager object and initialize it with the init_app()
  method and our application object app

Flask-Login provides us with a helpful decorator that we'll place on endpoints
we want to be protected. Remember, decorators allow us to run bits of code 
before ultimately running a function or in this case our flask endpoint.


@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  return render_template('user.html', user=user)


- the @login_required decorator is used to protect the user route

- the User table is queried for a user that matches the provided username

We will use this decorator on every Flask endpoint that we want only accessible by
logged in users. This will check to make sure the user login is still stored in
memory. So long as the user memory has not been cleared with a logout or browser
refreshing clear, the LoginManager() will be able to retrieve the identity of
the user before allowing them to access the information on that page.

We also need an additional helper function to load our individual user when 
trying to access protected routes.


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


- the load user() function loads a user with a given user_id

We can then login a user with a login route, paired with a login form, as shown
below:


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.check_password(form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page)
  if next_page else redirect(url_for('index', _external=True, _scheme='https')):
    else:
      return redirect(url_for('login', _external=True, _scheme='https'))
  return render_template('login.html', form=form)


- initialize a Loginform form

- if the form validates, query the User table for the user with an email that 
  matches the provided email

- if a user is found, user.check_password(form.password.data) checks the form
  entered password against the user's password

- if there is a match, login_user() logs user in and redirects to either
  next_page or the index route

- if no user is found or the password does not match, we redirect to the login
  route

'''

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager, login_required, login_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo

# instantiate aplication and database 
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# create login manager
login_manager = LoginManager()
login_manager.init_app(app)

# User model
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  joined_at = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
  
  def __repr__(self):
    return f'<User {self.username}'

  def set_password(self, password):
    return check_password_hash(self.password_hash, password)

# retistration form
class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')


# login form
class LoginForm(FlaskForm):
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  remember = BooleanField('Remember Me')
  submit = SubmitField('Login')

# registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm(csrf_enabled=False)
  if form.validate_on_submit():
    # define user with data from form here:
    user = User(username=form.username.data, email=form.email.data)
    # set user's password here:
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
  return render_template('register.html', title='Register', form=form)

# user loader
@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

# logint route
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm(csrf_enabled=False)
  if form.validate_on_submit():
    #query User here
    user = User.query.filter_by(email=form.email.data).first()
    # check if a user was found and the form password matches here:
    if user and user.check_password(form.password.data):
      # login user here:
      login_user(user)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('index', _external=True, _scheme='https'))
    else:
      return redirect(url_for('login', _external=True, _scheme='https'))
  return render_template('login.html', form=form)

# user route
@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  return render_template('user.html', user=user)

# landing page route
@app.route('/')
def index():
  # grab all guests and display them
  current_users = User.query.all()
  return render_template('landing_page.html', current_users=current_users)
 