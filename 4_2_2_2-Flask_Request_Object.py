# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 2. Flask Forms
# 2. Flask Request Object

'''
Every time a client communicates with a server it does so through a request. By
default our Flask routes only support GET requests. These are requests for data
such as what to display in a browser window. When submitting a form through a 
website, the form data is sent as a POST request. This type of request wants to add
data to the app. Routes can handle POST requests if it is specified in the methods
argument of the route() decorator.


@app.route("/", methods["GET", "POST"])


The code above shows a route that now supports both GET and POST requests. By
default methods is set to ["GET"]. When adding "POST" to route's methods, be
sure to include "GET" if you plan for th eroute to handle those requests as well.

Flask provides access to the data in the request through the request object.
Importing the request object allows us to access everything about the requests to
our app including form data and the request method such as GET and POST.


from flask import request


When data is sent via a form submission it can be access using the form attribute
of the request object. The form attribute is a dictionary with the form's field
names as the keys and the associated data as the values. For example, if a text
input had the name "my_text", then the data access would look like this:

text_in_field = request.form["my_text"]
'''

from flask import Flask, render_template, request
from helper4 import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
  new_id = len(recipes) + 1
  if len(request.form) > 0:
    recipes[new_id] = request.form["recipe"]
    descriptions[new_id] = request.form["description"]
    new_ingredients = request.form["ingredients"]
    new_instructions = request.form["instructions"]
    add_ingredients(new_id, new_ingredients)
    add_instructions(new_id, new_instructions)
  return render_template("index.html", template_recipes=recipes)

@app.route("/recipe/<int:id>")
def recipe(id):
  return render_template(
    "recipe.html",
    template_recipe=recipes[id],
    template_description=descriptions[id],
    template_ingredients=ingredients[id],
    template_instructions=instructions[id])

@app.route("/about")
def about():
  return render_template("about.html")
