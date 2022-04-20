# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 1. Flask Templates
# 1. Introduction

'''
When you navigate through a website you may notice that many of the pages 
on the site have a similar look and feel. This aspect of a website can be 
achieved with the use of templates. In this lesson the term template
refers to an HTML file that can represent multiple web pages with the same
structure and functionality.

We will be using the Flask framework for our application in this lesson. 
Flask uses the Jinja2 template engine (https://jinja.palletsprojects.com/en/2.11.x/)
to render HTML files that include application variables and control structures.
The Jinja2 template engine is a powerful tool that supports an organized and
growth oriented application.

In this lesson we will look at:

- How to organize our site file structure

- Use our application data with our templates

- Leverage control structures within our templates

- Share common elements across many templates

The application we will be building in the following exercises is a 
cookbook site that consists of a main page and individual recipe pages. 
Currently our app consists of 2 routes that return HTML strings for the
browser to display. Explore the application to begin your path to learning
templates!
'''

from flask import Flask
from helper2 import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  return '''
    <!DOCTYPE html>
    <html>
      <body>
        <h1>Cooking By Myself</h1>
        <p>Welcome to my cookbook. These are recipes I like.</p>
        <a href="/recipe/1">Fried Egg</a>
      </body>
    </html>
    '''

#### Add the variable `id` to the route URL
#### and make it the sole function parameter
@app.route("/recipe/<int:id>")
def recipe(id):
  return '''
    <!DOCTYPE html>
    <html>
      <body>
        <a href="/">Back To Recipe List</a>
        <p>names[id] = ''' + recipes[id] + '''</p>
        <p>descriptions[id] = ''' + descriptions[id] + '''</p>
        <p>ingredients[id] = ''' + str(ingredients[id]) + '''</p>
        <p>instructions[id] = ''' + str(instructions[id]) + '''</p>
      </body>
    </html>
    '''