# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 2. Flask Forms
# 7. Validation

'''
In order to submit a form, it is common that certain required text fields must
have data, date fields need to have a specific format, or a checkbox agreeing
to certain terms needs to be checked.

Validation is when form fields must contain data or a certain format of data
in order to move forward with submission. We enable validation in our form
class using the validators parameter in the form field definitions.

Validators come from the wtform.validators module. Importing the DataRequired()
validator is accomplished like this:


from wtforms.validators import DataRequired


The DataRequired() validator simply requires a field to have something in it 
before the form is submitted. Notifying the user that data is required is
handled automatically.


my_textfield = StringField("TextLabel", validators=[DataRequired()])


The validators argument takes a list of validator instances.

The FlaskForm class also provides a method called validate_on_submit(), which
we can use in our route to check for a valid form submission:


if my_form.validate_on_submit():
  # get form data
  

As we saw in second exercise pertaining to the request object, in order to avoid
gathering data on first access to the route we had to put the data gathering
code inside an if statement. The validate_on_submit() function does this 
exact task.

The validate_on_submit() function returns True when there is a POST request and
all the associated form validators are satisfied. At this point the data can be
gathered and processed. When the function returns False the route function can
move onto other tasks such as rendering the template.
'''

from flask import Flask, render_template, request
from helper5 import recipes, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

class CommentForm(FlaskForm):
  comment = StringField("Comment", validators=[DataRequired()]) # remember to validate!
  submit = SubmitField("Add Comment")

@app.route("/", methods=["GET", "POST"])
def index():
  return render_template("index.html", template_recipes=recipes)

@app.route("recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  comment_form = CommentForm(csrf_enabled=False)
  if comment_form.validate_on_submit():
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