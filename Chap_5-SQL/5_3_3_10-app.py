# 5. Introduction to SQL and Databses for Back-End Web Apps
# 3. Databases in Flask
# 3. Databases in Flask - Reading, Updating and Deleting
# 10. Review

# app.py


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #to supress warning
db = SQLAlchemy(app)

#declaring the Book model
class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True) #primary key column
  title = db.Column(db.String(80), index=True, unique=True) #book title
  author_name = db.Column(db.String(50), index=True, unique=False)
  author_surname = db.Column(db.String(80), index=True, unique=False)
  month = db.Column(db.String(20), index=True, unique=False)
  year = db.Column(db.Integer, index=True, unique=False)
  reviews = db.relationship('Review', backref='book', lazy='dynamic', cascade='all, delete, delete-orphan') #relationship of Books and Reviews
  annotations = db.relationship('Annotation', backref='book', lazy='dynamic', cascade='all, delete, delete-orphan')
  
  def __repr__(self):
    return f'{self.id} in: {self.month},{self.year}'

#add your colums for the Reader model
class Reader(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), index=True, unique=False)
  surname = db.Column(db.String(80), index=True, unique=False)
  email = db.Column(db.String(120), index=True, unique=True)
  reviews = db.relationship('Review', backref='reviewer', lazy='dynamic', cascade='all, delete, delete-orphan')
  annotations = db.relationship('Annotation', backref='author', lazy='dynamic', cascade='all, delete, delete-orphan')
  
  def __repr__(self):
    return f'Reader ID: {self.id}, email: {self.email}'

#declaring the Review model
class Review(db.Model):
  id = db.Column(db.Integer, primary_key=True) #primary key column, automatically generated IDs
  stars = db.Column(db.Integer, unique=False)
  text = db.Column(db.String(200), unique=False)
  book_id = db.Column(db.Integer, db.ForeignKey('book.id')) #foreign key column
  reviewer_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
  
  def __repr__(self):
    return f'Review ID: {self.id}, {self.stars} stars, {self.book_id}'

#declaring the Annotation model
class Annotation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  text = db.Column(db.String(200), unique=False)
  review_id = db.Column(db.Integer, db.ForeignKey('reader.id'))
  book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
  
  def __repr__(self):
    return f'<Annotation {self.reviewer_id}-{self.book_id}:{self.text}'
  
  import routes  
  