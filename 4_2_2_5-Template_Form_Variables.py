# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 2. Flask Forms
# 5. Template Form Variables

'''
Creating a form in the template is done by accessing attributes of the form
passed to the template.

Let's use the following form as we work toward implementing it in a template:


class MyForm(FlaskForm):
  my_textfield = StringField("TextLabel")
  my_submit = SubmitField("SubmitName")


In our application route we must instantiate the form and assign that
instance to a template variable:


my_form = MyForm()
return render_template(template_form=my_form)


Moving to the template, creating a form we simply use the form class attributes
as expressions.


<form action="/" method="POST">
  {{ template_form.hidden_tag() }}
  {{ template_form.my_textfield.label }}
  {{ template_form.my_textfield() }}
  {{ template_form.my_submit() }}
</form>


Inside the standard <form> are all the FlaskForm objects access through 
template_form.

The first line {{ template_form.hidden.tag() }} is the other end of the CSRF
protection. While not visibiel in the form, this field handles the necessary
tasks to protect from CSRF.

The next two lines are for the text box. The first accesses the label of the field,
which we specified as an argument when we created the field. The second 
my_textfield line is the input field itself.

The last line of the form is the submit button. Just like the HTML version, this
will initiate sending the form data back to the server.

The HTML created from this form implementation is as follows:


<form action="/" method="post">
  <input id="csrf_token" name="csrf_token" type="hidden" value="ImI1YzIxZjUwZWMxNDg0ZDFiODAyZTY5M2U5MGU3MTg2OThkMTJkZjQi.XupI5Q.9HOwqyn3g2pveEHtJMijTu955NU">
  <label for="my_textfield">TextLabel</label>
  <input id="my_textfield" type="text" value="">
  <input id="my_submit" name="my_submit" type="submit" value="SubmitName">
</form>

'''

# This is still soo confusing. Not really the task at hand, but all the files,
# back and forth. Nestinggalore. Gonna take some time to get this in...

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
    template_descriptions=descriptions[id],
    template_ingredients=ingredients[id],
    template_instructions=instructions[id],
    template_comments=comments[id],
    template_form=comment_form)

@app.route("/about")
def about():
  return render_template("about.html")

