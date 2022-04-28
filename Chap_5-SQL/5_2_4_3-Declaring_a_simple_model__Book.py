# 5. Introduction to SQL and Databses for Back-End Web Apps
# 2. Queries
# 4. Databases in Flask
# 3. Declaring a simple model: Book

''' 
The database object db created in our application contains all the functions and
helpers from both SQLAlchemy and SQLAlchemy Object Relational Mapper (ORM).
SQLAlchemy ORM assoiates user-defined Python classes with database tables, and
instances of those classes (objects) with rows in their corresponding tables. 
The classes that mirror the database tables are referred to as models.


We would like to create a Flask-SQLAlchemy ORM representation of the following
table schema:

Book
ID                INTEGER
TITLE             STRING
Author name       STRING
Author surename   STRING
Month             STRING
Year              STRING

The key symbol represents the primary key column that denotes a column or a 
property that uniquely identifies entries in the table. For example, student
number, social security number, SKU (stock keeping unit), ISBN (International
Standard Book Number), and similar, often serve as primary keys. 

Model represents a declarative base in SQLAlchemy which can be used to declare
models. For Book to be a database model for the database instance db, it has to
inherit from db.Model in the following way:


class Book(db.Model):


As you can see in the code editor, the Book model has 5 attributes of Column 
class. The types of the column are the first argument to Column. We use the
following column types:

- String(N), where N is the maximum number of characters

- Integer, representing a whole number

Column can take some other parameters:

- unqie: when True, the values in the column must be unique

- index: when True, the column is searchable by its values

- primary_key: when True, the column serves as the primary key

'''

# Again that overwhelming feel lol. Never ending story!


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS'] = False

class Book(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), index = True, unique = True)
  author_name = db.Column(db.String(50), index, True, unique = False)
  author_surename = db.Column(db.String(80), index = True, unique = False)
  month = db.Column(db.String(20), index = True, unique = False)
  year = db.Column(db.Integer, index = True, unique = False)
  
  # Get a nice printout for Book objects
  def __repr__(self):
    return f'{self.title} in: {self.month},{self.year}'

@app.route('/')
@app.route('/home')
def home():
  return 'Congrats! You have just made your first Flask-SQLAlchemy model declaration!'
  