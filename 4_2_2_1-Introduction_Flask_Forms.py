# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 2. Flask Forms
# 1. Introduction

'''
An important role of websites is gathering information from the user. Wether
a user is signing into their Codecademy account, ordering clothes online or
leaving feedback for a company, web forms have provided a simple way to enter
and submit data over the internet.

The use of forms in a site can be an involved process. The designer must
gather the right information, display the fields in a pleasing manner and ensure
the data is collected correctly. Over the years this has become easier thanks
to frameworks like Flask, which help streamline the process of displaying 
fields and gathering data.

This lesson assumes a foundational knowledge of web forms and the steps involved
in sending the data to the web server. In the following exercises we are going
to look at how Flask can help gather data from regular web forms as well as 
create forms in an entirely new way.
'''

'''
To help us learn about forms we will be using a cookbook app that lists recipes
on a main page and links to individual recipe pages.

- The main Flask app is contained in app.py and has three routes: index, recipe
  and about. The index route has method POST added to andle form submissions.

- The file helper.py contains the mock data for the app and has two functions, 
  add_ingredients() and add_instructions() to help populate the data.

- The main web page is rendered from the template index.html. There is a title, 
  list of recipes and a new recipe form. The form has fields for the recipe
  name, description, ingredients and instructions.

- The other template is recipe.html which renders each individual recipe 
  using the mock data. 

Review the site structure and head to the next exercise when you're ready.
'''

# Just noting down index.html and the app.py for now. And added another helper
# helper4.py

from flask import Flask, render_template
from helper4 import recipes, descriptions, ingredients, instructions

@app.route("/")
def index():
  return render_template("index.html", template_recipes=recipes)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe():
  return render_template(
    "recipe.html",
    template_recipe=recipes[id],
    template_description=descriptions[id],
    template_ingredients=ingredients[id],
    template_instructions=instructions[id]
  )

@app.route("/about")
def about():
  return render_template("about.html")