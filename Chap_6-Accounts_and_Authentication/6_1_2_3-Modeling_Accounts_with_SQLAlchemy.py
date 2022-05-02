# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 2. Introduction to Accounts
# 3. Modeling Accounts with SQLAlchemy

''' 
When creating a user account in an application, there are a varity of data that
needs to be stored for each user, as well as associated methods. The best way
to store this data for a Flask application is as a model in a database managed
by Flask-SQLAlchemy.

There are some fileds we might want to store for each of our users no matter what
kind of application we are creating. For example, these fields can include.
id, username, email, password_hash, and joined_at_date. A good way to store this
data is in a User model within your database. For example, given some database
db:


class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))
  joined_at_date = db.Column(db.DateTime(), index=True,default=datetime.utcnow)


- here we instantiate a model User

- that stores primary key id as an Integer

- username, email and password_hash as Strings, and

- joined_at_date as a DateTime

In addition to this informational data, we want to add methods that represents
different user needs. We could write these methods ourselfs, but Flask-Login
does that work for us with the help of mixins. Mixins help us inject some standard
code into a class to make life easier. In this case, we will inherit the methods
and properties of the UserMixin class.


from flask_login import UserMixin

class User(UserMixin, db.Model)


- when we inherit from UserMixin, we inherit some of the following functions:
  is_active(), is_authenticated(), is_anonymous()

- these functions will be helpful later on for understanding the state of our
  users.

'''

from datetime import datetime
from flask import Flask
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# instantiate application and database
app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///my_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# update User to inherit from UserMixin here:
class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True, unique=True)
  # add the email and password_hash attributes here:
  email = db.Column(db.String(120), index=True, unique=True)
  password_hash = db.Column(db.String(128))

  # add the joined_at attribute here
  joined_at = db.Column(db.DateTime(), index=True, default=datetime.utcnow)
