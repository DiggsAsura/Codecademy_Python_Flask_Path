# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 1. Flask Templates
# 3. Template Variables

'''
Instead of having an HTML file for each recipe, it would be a lot easer having 
one file for many recipes. Being able to pass data to template files is how
we can begin to accomplish this goal. 

After the filename argument in render_template() we can add keyword arguments to
be used as variables within the template. These variables are assigned values
or app data we would like to access within the template.


flask_variable = "Text for my template"

render_template("my_template.html", template_variable=flask_variable)


In this example we're assigning the value of flask_variable to template_variable
which can be used in my_template.html. To add more than one variable separate
each assignment with a comma.


render_template("my_template.html", template_var1="A string!", template_var2=100)


Our template now has access to the variables template_var1 and template_var2 which
hold a string and an integer respectively.

App data can be passed as literal values or the values stored inside variables. We
can pass strings, integers, lists, dictionaries or any other object to our
templates.

It is possible to give keyword arguments and the assignment variables the same
name var1=var1. For these exercises all variables from our flask app will start
with flask and all template variables will start with template.

To access the variables in our templates we need to use the expression 
delimiter: {{}}.


{{ template_variable }}


The delimiter can be used inline with text and alongside HTML elements.


<h1>My Heading: {{ template_variable }}
</h1>


Certain operations can be performed inside expression delimiters {{}}.

With template_variable = 20.


<p>Template number plus ten: {{ template_variable + 10 }}</p>

OUTPUT
Template number plus ten: 30


List and dictionary elements can be accessed individually inside the expression
delimiters {{}}

With template_list = "["A", "B", "C"]


<p>Element at index 1: {{ template_list[1] }}

OUTPUT
Element at index 1: B

'''

from flask import Flask, render_template
from helper3 import recipes, descriptions, ingredients

app = Flask(__names__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/recipe/<int:id>')
def recipe(id):
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id])

