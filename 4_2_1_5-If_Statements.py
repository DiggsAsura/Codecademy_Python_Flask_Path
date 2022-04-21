# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 1. Flask Templates
# 5. If Statements

'''
Including conditionals such as if and if/else statements in our templates
allows us to control how data is handled. 

Let's say we have a string variable passed to our template. When the variable
contains an empty string will you want to output it our will you want to 
output another string? Remember the default filter doesn't work in this 
situation so an if statement is needed.

Using if statements in a template happens inside  delimiter block: {% %}

{% if condidtion %}
  <p>This text will output if condition is True</p>
{% endif %}

Notice the {% endif %} delimiter is necessary to close the if satement.

The condition can include a variable that is tested using statndard comparison
operators, <, >, <=, >=, ==, !=.

{% if template_variable == "Hello" %}
  <p>{{template_variable}}, World!</p>
{% endif %}

While inside statement delimiters {% %} we can access variables whitout using
the usual expression delimiter {{ }}.

Variables can also be tested on their own. A variable defined as None or False
or equates to 0 or contains an empty sequence such as "" or [] will test as
False. 

The {% else %} and {% elif %} delimiters can be included to create multi-branch
if statements. 

Given the assignment template_number = 20.

{% if template_number < 20 %}
  <p>{{ template_number }} is less than 20.</p>
{% elif template_number > 20 %}
  <p>{{ template_number }} is greater than 20.</p>
{% else %}
  <p>{{ template_number }} is equal to 20.</p>
{% endif %}

OUTPUT
20 is equal to 20.

As expected the {% else %} branch is the one that is followed.
'''


# This exercise is done in the html file

from flask import Flask, render_template
from helper3 import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/recipe/<int:id>')
def recipe(id):
  return render_template("recipe.html", template_recipe=recipes[id], template_description=descriptions[id], template_ingredients=ingredients[id], template_instructions=instructions[id])