# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 1. Flask Templates
# 7. Inheritance

'''
If you go to any website you may notice certain elements exist across different 
web pages.

The navigation bar is a good example of a common page element. This is the 
banner at the top of most sites that has links to different pages. No matter
what page you're on the navigation bar is there.

Imagine having separate files for each web page and wanting to make a change
to the navigation bar. Would you have to change the content of every template of
the site? No, that would take too long.

To solve this problem template files are used to share content across multiple
templates. The simplest case is a file that includes the top portion of the 
templates through the <body> tag and then the closing </body> and </html> tags.
Jinja2 statement delimiters are then used to identify the area of the template
where specific content will be substituted in.


<html>
  <head>
    <title>MY WEBSITE</title>
  </head>
  <body>
  {% block content %}{% endblock %}
  </body>
</html>


For this exercise we will name the above template base.html.

To inherit this content in another template we will use the extends statement.
The code to be substituted should then be surrounded by {% block content %} and
{% endblock %}. All together this looks like the following template:


{% extends "base.html" %}

{% block content %}
  <p>This is my paragraph for this page.</p>
{% endblock %}


This template is named index.html.

When a route returns render_template("index.html") the rendered page will have
this content.
'''

# Here again, all exercises is in the html files. I still write the app.py (this file)
# to not forget/try to internalize how the base is done.

from flask import Flask, render_template
from helper3 import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  return render_template("4_2_1_7-index.html")

@app.route('/recipe/<int:id>')
def recipe(id):
  return render_template("4_2_1_7-recipe.html",
                         template_recipe=recipes[id],
                         template_description=descriptions[id],
                         template_ingredients=ingredients[id],
                         template_instructions=instructions[id])
  