# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 2. Flask Forms
# 4. FlaskForm Class

'''
Flask provides an alternative to web forms by creating a form class in the
application, implementing the fields in the template and handling the data
back in the application.

A flask form class inherits from the class FlaskForm and includes attributes
for every field:


classMyForm(FlaskForm):
  my_textfield = StringField("TextLabel")
  my_submit = SubmitField("SubmitName")


This simple class enable the creation of a form with a text field and a submit
button.

The class inherits from a class FlaskForm which allows to implement the form
as template variables and then collect the data once submitted. FlaskForm
is part of FlaskWTF.
https://flask-wtf.readthedocs.io/en/0.15.x/

Access to the fields of this form class is done through the attributes, 
my_textfield and my_submit. The StringField and SubmitField classes are the 
same as <input type=text....> and <input type=submit...> rescpectively and
are part of the WTForms library.
https://wtforms.readthedocs.io/en/2.3.x/

Below is a simple Flask app with the form class.


from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, Submitfield

app = Flask(__name__)
app.config("SECRET_KEY") = "my_secret"

class MyForm(FlaskForm):
  my_textfield = StringField("TextLabel")
  my_submit = SubmitField("SubmitName")
  
@app.route("/")
def my_route():
  flask_form = MyForm()
  return render_template("my_template", template_form=flask_form)


First note the new import statements. FlaskForm is imported from the flask_wtf
module and both form fields import from wtforms.

The next new line is:

app.config["SECRET_KEY"] = "my_secret"

This line is a way to protect against CSRF or Cross-Site Request Forgery. Without
going into too much detail, CSRF is an attack that used to gain control of a 
web application.

Next is the MyForm class definition. It inherits from FlaskForm and has attributes
for the text and submit fields. For each field the label is passed as the 
only argument.

Lastly, in order to use this form in our template, we must create an instance of
it and pass it to the template using render_template(). We will look at 
applying the form in the template in the next exercise. 
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
  return render_template("index.html", template_recipes=recipes)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  comment_form = CommentForm()
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