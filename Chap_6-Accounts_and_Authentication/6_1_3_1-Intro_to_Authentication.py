# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 3. Introduction to Authentication with Flask
# 1. Intro to Authentication

'''
Authentication is the process of verifying that an individual has permission to 
perform an action. Without authentication, there would be no way of knowing or
enforcing access control on our browser for our applications.

Our strategy of authenticating users depends on discerning wheter a password
is valid or not in order to allow the user to perform further actions in the
application.

In the next lesson we'll get to know some of the tools that we can use to 
authenticate in Python Flask applications by building a web application that 
allows authenitcated users to view an awesome secret recipe.

Click Next to get started
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, Authentication World!'