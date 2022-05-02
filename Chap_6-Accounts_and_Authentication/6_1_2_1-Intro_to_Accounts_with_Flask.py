# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 2. Introduction to Accounts
# 1. Intro to Accounts with Flask

''' 
Accounts are the end result of gathering data necessary to create a user for a 
website. They also allow you to keep logging in to use the application.

Ever wonder what the process would be to create a site that featured user accounts?
Well wonder no further! By the end of this lesson you will be familiar with the 
concepts and code necessary to create a web application with user account 
functionality.

Remember Flask is a micro-framework with web server functionality and built in
tools to make web development simple and enjoyable. Along the way we will use
other Flask tools to address our development needs.

We will be using Flask's Flask-Login, SQLAlchemy and WTForms Python packages
to build our application. The application will allow you to invite your friends
to a dinner party, and users will have the power to login and RSVP for the 
fun evening. We'll call it DinnerParty! The sooner we start, the sooner us and
our friends will be enjoying desserts!
'''

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, DinnerParty!'