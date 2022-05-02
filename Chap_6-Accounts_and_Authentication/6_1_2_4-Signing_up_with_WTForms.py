# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 2. Introduction to Accounts
# 4. Signing up with WTForms

''' 
Now that we've got a database setup, our dinner application is starting to take
shape. We're going to need to get some data from our friends in order to make
their dinner party accounts.

We could get all kinds of juicy information from them like their favorite dish or
favorite chef, but for now, we'll just grab their email address, username, and 
password. To get this information we'll need to provide the user with an interface
that has input areas for the respective fields that need to be filled out. An
HTML form is a perfect way to gather this data!

We will use WTForms to create forms that make it easy for us to grab the data we
need.


classRegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')


- a class RegistrationForm is defined and inherits from FlaskForm

- StringFields username and email are defined with the appropriate validators

- PasswordFields password and password2 are defined with the appropriate 
  validators to ensure the same password is entered twice

- a SubmitField named submit is defined

And we will have a route that allows the users to create an account.


@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    return render_template('register.html', form=form)


- a RegistrationForm named form is created

- if the form is validated upon submission, a User named user is created with a
  username and email from the form data

- the user's password is set and hashed using the set_password method

- the user is added to the database session and the session is commited

Lastly, we need to make sure to update our template file to make sure the form 
is displayed properly to our users.
'''

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

# instantiate application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User model
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), unique=True, index=True)
  password_hash = db.Column(db.String(128))
  joined_at = db.Column(db.DateTime(), default=datetime.utcnow, index=True)

  def __repr__(self):
    return f'<User {self.username}'
  
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)

# registration form
class RegistrationForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired(), Email()])
  password = PasswordField('Password', validators=[DataRequired()])
  password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

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

# landing page route
@app.route('/')
def index():
  # grab all guests and display them
  current_users = User.query.all()
  return render_template('landing_page.html', current_users=current_users)
