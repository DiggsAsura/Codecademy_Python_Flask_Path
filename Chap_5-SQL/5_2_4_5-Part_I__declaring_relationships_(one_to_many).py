# 5. Introduction to SQL and Databses for Back-End Web Apps
# 2. Queries
# 4. Databases in Flask
# 5. Part I: declaring relationships (one-to-many)

''' 
Often times a real-world applications we will have entities that are somehow
related. Students take courses, customers buy products, and users comment on 
posts. In SQLAlchemy we can declare a relationship with a field initialized with
the .relationship() method. In one-to-many relationships, the relationship field
is used on the 'one' side of the relationship. In our use case we have the following
one-to-many relationships:

1. One book ---< many reviews for that book 

2. One reader ---< many reviews from that reader

Hence, we add relationship fields to the Book and Reader models. In this exercise,
we will show you how to add a relationship to the Book model, and you will do the 
same for the Reader model.

We declare a one-to-many relationship between Book and Review by creating the 
following field in the Book model:


reviews = db.relationship('Review', backref='book', lazy='dynamic')


where

- the first argument denotes which model is to be on the 'many' side of the
  relationship: Review
  
- backref = 'book' establishes a book attribute in the related class (in our case,
  class Review) which will serve to refer back to the related Book object.

- lazy = dynamic makes related objects load as SQLAlchemy's query objects.

By adding relationship to Book we only handle one side in our one-to-many 
relationship. Specifically, we only covered the direction denoted by the red arrow
in the schema below:

See 5_2_4_5-book-review.jpg

In the next exercise, we will add the Review model and its relationship with the
Book model (the blue arrow).

'''

# FML hard life

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
  reviews = db.relationship('Review', backref='book', lazy='dynamic')
  
  def __repr__(self):
    return f'{self.title} in : {self.month},{self.year}'


class Reader(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), index=True, unique=False)
  surname = db.Column(db.String(80), index=True, unique=False)
  email = db.Column(db.String(120), index=True, unique=True)
  reviews = db.relationship('Review', backref='reviewer', lazy='dynamic')
  
  def __repr__(self):
    return f'Reader: {self.email}'



@app.route('/')
@app.route('/home')
def home():
  return 'Congrats! You are making your first one-to-many relationship in Flask-SQLAlchemy!'

