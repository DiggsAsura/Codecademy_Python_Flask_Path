# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 3. Introduction to Authentication with Flask
# 2. Meet Flask-Login

'''
When building web applications we might first start with the base of our 
application serving and endpoint saying "Hello World".


from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello Authentication World!'


The application we will be building will show how to use tools in Flask to
authenticate users. The primary tool we can use to achieve our purposes of 
authenticating in Flask is Flask-Login
https://flask-login.readthedocs.io/en/latest/

Flask-Login is a third-party package that allows us to use pieces of code that
enable us to perform authentication actions in our application.

We can manage user logins with the LoginManager object from within Flask-Login,
as shown below:


from flask_login import LoginManager


- LoginManager is imported from the flask_login package

- a new LoginManager object named login_manager is created

Once a LoginManager object is defined, we need to initialize the manager with
our application. This can be done with the init_app() method of a LoginManager:


login_manager.init_app(app)


- our instance of LoginManager, login_manager, calls its init_app() method
  with app, an initialized Flask app, as an argument
'''

from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

@app.route('/')
def hello_world():
  return 'Hello, Authentication World!'