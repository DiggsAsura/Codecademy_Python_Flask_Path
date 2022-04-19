# 4. Introduction to Flask
# 1. Introduction to Flask
# 3. Build Your First Flask App
# 2. Instantiate Flask Class

'''
We'll now break down each step in creating a minimal Flask app. The Python module
that contains all the classes and functions needed for building a Flask app is 
called flask.

We can begin building our app by importing the Flask class, which is needed to 
create the main application object, from the flask module:

# from flask import Flask

Now, we can create an instance of the Flask class. Let's save the application object
in a variable called app:

# app = Flask(__name__)

When creating a Flask object, we need to pass in the name of the application.
In this case, because we are working with a single module, we can use the
special Python variable, __name__.

The value of __name__ depends on how the Python script is executed. If we run
a Python script directly, such as with python_app.py in the terminal, then
__name__ is equal to the string '__main__'. On the other hand, if the script
is being imported as a module into another Python script, then __name__ would be
equal to its filename.

As we'll see in the next exercise, this distinction can be useful when we have
code that we want to be run only if the script is executed a particular way.
'''

from flask import Flask

app = Flask(__name__)

print(__name__)
print(app)