# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 1. Flask Templates
# 8. Review

'''
Congratulations, this concludes the lesson on Flask templates. In this
lesson we:

- Created a file structure that works with the Jinja2 template engine

- Rendered pages in our browser using files called templates

- Shared our application data for use within templates

- Applied filters to our data within our templates

- Utilized if statements to bring decision making to our templates

- Implemented for loops to perform repetitive tasks in our templates

- Moved common content to separate files to be shared by many templates

To show the power of what we have learned let's add a simple navigation
bar to the app!

'''

from flask import Flask, render_template
from helper3 import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/about')
def about():
  return render_template("about.html")

@app.route('/recipe/<int:id>')
def recipe(id):
  return render_template("recipe.html",
  template_recipe=recipes[id],
  template_description=descriptions[id],
  template_ingredients=ingredients[id],
  template_instructions=instructions[id])
