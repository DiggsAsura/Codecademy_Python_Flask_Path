#5. Introduction to SQL and Databses for Back-End Web Apps
#2. Queries
#4. Databases in Flask
#2. Flask application with Flask-SQLAlchemy

''' 
Flask-SQLAlchemy is an extension for Flask that supports the use of a Python
SQL Toolkit called SQLAlchemy.

To start creating a minimal application, in addition to importing Flask, we also
need to import SQLAlchemy class from flask_sqlalchemy module:


from flask import Flask
from flask_sqlalchemy import SQLAlchemy


The next step is to create our Flask app instance:


app = Flask(__name__)


To enable communication with a database, the Flask-SQLAlchemy extension takes 
the location of the application's database from the SQLALCHEMY_DATABASE_URI 
configuration variable we set in the following way:


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db'


Next, we set the SQLALCHEMY_TRACK_MODIFICATIONS configuration option to False to
disable a feature of Flask-SQLAlchemy that signals the application every time
a change is about to be made in the database.


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


Finally, we create an SQLAlchemy object and bind it to our app:


db = SQLAlchemy(app)

'''


from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# database configuration
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///myDB.db' # path to database and its name
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # to supress warning
db = SQLAlchemy(app) # database-instance



# some routing for displaying the home page
@app.route('/')
@app.route('/home')
def home():
  return 'Congrats! You have just created your first Flask application supporting databases!'

