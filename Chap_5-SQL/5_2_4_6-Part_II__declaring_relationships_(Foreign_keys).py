# 5. Introduction to SQL and Databses for Back-End Web Apps
# 2. Queries
# 4. Databases in Flask
# 6. Part II: declaring relationships (Foreign keys)

'''
In the previous lesson, we began adding a one-to-many relationship to the Book and
Reader models by using .relationship(). But that does not completly specify our
one-to-many relationship. We additionally have to specify what the forign keys
are for the model on the 'many' side of the relationship. To remind you, a foreign
key is a field (or collection of fieldds) in one table that refers to the primary
key in another table.

In this exercise we want to create the following database schema:

see 5_2_4_6-reader-book-reivew.jpg

To complete the schema, we need to add the Review model, and specify the foreign
keys (blue arrows) representing the following relationship:

- One review --- one book for which the review was written

- One review --- one reader who wrote that review

The red arrows were covered in the previous exercise with the db.relationship()
columns.

Similar to the previous models we declared, the Review model has its own columns
such as text, stars (denoting ratings), and its own primary key field id.
Review additionally needs to specify which other models it is related to by
specifying their primary key in its foreign key column:


book_id = db.Column(db.Integer, db.ForeignKey('book.id'))


The book_id field is a forign key that refers to the primary key id of the Book
table. Similar to the primary key, a foreign key is just another column in our
model with unique entries.
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
  reviews = db.relationship('Review', backref='book', lazy='dynamic')
  
  def __repr__(self):
    return f'{self.title} in: {self.month},{self.year}'

class Reader(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(50), index=True, unique=False)
  surname = db.Column(db.String(80), index=True, unique=False)
  email = db.Column(db.String(120), index=True, unique=True)
  reviews = db.relationship('Review', backref='reviewer', lazy='dynamic')
  
  def __repr__(self):
    return f'Reader: {self.email}'

class Review(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  stars = db.Column(db.Integer, unique=False)
  text = db.Column(db.String(200), unique=False) # a review's text here below is the forign key column linking to the primary key (id) of the book model (book). Note the lower case here: book.id instead of Book.id
  book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
  reviewer_id = db.Colum(db.Integer, db.ForeignKey('reader.id'))
  
  def __repr__(self):
    return f'Review {self.text} stars: {self.stars}'


@app.route('/')
@app.route('/home')
def home():
  return 'Congrats! You have just made a forign key column in your Flask-SQLAlchemy model!'

# but dont understand shit anyways lol

