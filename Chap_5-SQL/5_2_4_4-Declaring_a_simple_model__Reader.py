# 5. Introduction to SQL and Databses for Back-End Web Apps
# 2. Queries
# 4. Databases in Flask
# 4. Declaring a simple model: Reader

'''
Adding another model or table schema to your application is simple. You only need
to create another class that inherits from Model.

The model you will create next, Reader, is simple and similar to Book. Let us
try it together. You can do this!

To make it easier for you, here's the schema representation of Reader:

Reader
ID            INTEGER
NAME          STRING
SURENAME      STRING
EMAIL         STRING

We have already provided the Reader class declaration and the representation 
method.

'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), index=True, unique=True)
  author_name = db.Column(db.String(50), index=True, unique=False)
  author_surname = db.Column(db.String(80), index=True, unique=False)
  month = db.Column(db.String(20), index=True, unique=False)
  year = db.Column(db.Integer, index=True, unique=False)
  
  def __repr__(self):
    return f'{self.title} in: {self.month},{self.year}'


class Reader(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), index=True, unique=False)
  surname = db.Column(db.String(80), index=True, unique=False)
  email = db.Column(db.String(120), index=True, unique=True)
  
  def __repr__(self):
    return f'Reader: {self.email}'

  