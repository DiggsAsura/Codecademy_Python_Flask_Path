# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 1. Flask Templates
# 6. For Loops

'''
Repetitive tasks are standard in most computer applications and template rendering is
no different. Creating lists, tables or group of images are all repetitive tasks
that can be solved using for loops.

Using the same statement delimiter block as if statetmens {% %]}, for loops step through
a range of numbers, lists and dictionaries.

The following code will create an ordered list where each line will output the 
index of the sequence:


<ol>
{% for x in range(3) %}
  <li>{{ x }}</li>
{% endfor %}

OUTPUT
1. 0
2. 1
3. 2


The syntax is similar to a Python for loop where we define a loop variable x to 
step through a series of numbers using range(3). The local loop variable can
be used inside our loop with the expression delimiter {{x}}

Similar to the if statements we need to close the loop with an {%endfor%} block.

The following are a few more applications of a for loop.

Iterate through a list variable:
{% for element in template_list %}

Iterate through a String
{% for char_in_string "Hello!" %}

Iterate through the keys of a dictionary variable:
{% for key in template_dict %}

Iterate through keys AND values of a dictionary with items():
{% for key, value in template_dict.items() %}

Using the filter dictsort in a loop outputs the key/value pairs just like items()


'''

# This task is done in the html files

from flask import Flask, render_template
from helper3 import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html", template_recipes=recipes)

@app.route('/recipe/<int:id>')
def recipe(id):
  return render_template("recipe.html",
  template_recipe=recipes[id],
  template_description=descriptions[id],
  template_ingredients=ingredients[id],
  template_instructions=instructions[id])

