# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 2. Flask Forms
# 6. Handling FlaskForm Data

'''
Once a form is submitted, the data is sent back to the server through a POST
request. Previously we covered accessing this data through the request 
object provided by Flask.

Using our FlaskForm class, data is now accessible through the form instance in
the Flask app. The data can be directly accessed by using the data attribute
associated with each field in the class.


form_data = flask_form.my_textfield.data


Keeping all the information and functionality attached to the form object
has streamlined the form creation and data gathering process.

Remember that when a route handles a form it is necessary to add the POST
method to the route decorator.


methods=["GET", "POST"]
'''

from flask import Flask, render_template, request
from helper5 import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

class CommentForm(FlaskForm):
  comment = StringField("Comment")
  submit = SubmitField("Add Comment")
  
@app.route("/", methods=["GET", "POST"])
def index():
  return render_template(
    "index.html",
    render_recipes=recipes)

@app.route("/recipes/<int:id>", methods=["GET", "POST"])
def recipe(id):
  comment_form = CommentForm()
  new_comment = comment_form.comment.data
  comments[id].append(new_comment)
  return render_template(
    "recipe.html",
    template_recipe=recipes[id],
    template_description=descriptions[id],
    template_ingredients=ingredients[id],
    template_instructions=instructions[id],
    template_comments=comments[id],
    template_form=comment_form)

@app.route("/about")
def about():
  return render_template("about.html")