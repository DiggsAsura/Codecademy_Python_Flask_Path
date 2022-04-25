# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 2. Flask Forms
# 9. Redirecting

'''
Beside rendering templates from our routes, it can be important to move from
one route to another. This is the role of the function redirect().

Consider the case where we create our form in one route, but after the form
submission we want the user to end up in another route. While we can set the
action attribute in the HTML <form> tag to go any path, redirect() is the
best option to move from one route to another.


redirect("url_string")


Using this function inside another route will simply send us to the URL we specify.
In the case of a form submission, we can use redirect() after we have processed
and saved our data inside our validate_on_submit() check.

Why don't we just render a different template after processing our form data?
There are many reasons for this, one being that each route comes with its own
business logic prior to rendering its template. Rendering a template outside
the initial route would mean you need to repeat some or all of this code.

Once again, to avoide possible URL string pitfalls, we can utilize url_for() within
redirect(). This allows us to navigate routes by specifying the route function
name instead of the URL path.


redirect(url_for("new_route", _external=True, _scheme='https'))


- we must add two new keyowrd arguments to our call of url_for()

- the keyword arguments _external=True and _scheme='https' ensure that the URL
  we redirect to is a secure HTTPS address and not an insecure HTTP address

Similarly, regular keyword arguments can be added if necessary.


redirect(url_for("new_route", new_var=this_var, _external=True, _scheme='https'))

'''

# Bah back to brain wrinkles again. I mean I do understand bits and pieces, it's
# just so many of them. Struggle to beleive I can make something out of this
# currently, but let's go. 

from flask import Flask, render_template, request, redirect, url_for
from helper5 import recipes, types, descriptions, ingredients, instructions, add_ingredients, add_instructions, comments
from forms import RecipeForm, CommentForm

app = Flask(__namø__)
app.config['SECRET_KEY'] = 'mysecret'

@app.route('/', methods=["GET", "POST"])
def index():
  recipe_form = RecipeForm(csrf_enabled=False)
  if recipe_form.validate_on_submit():
    new_id = len(recipes)+1
    recipes[new_id] = recipe_form.recipe.data
    types[new_id] = recipe_form.recipe_type.data
    descriptions[new_id] = recipe_form.descriptions.data
    new_ingredients(new_id, new_ingredients)
    new_instructions(new_id, new_instructions)
    comments[new_id] = []
    ### Task
    return redirect(url_for("recipe", id=new_id, _external=True, _scheme='https'))
  
  return render_template("index.html", template_recipes=recipes, template_form=recipe_form)

@app.route("/recipe/<int:id>", methods=["GET", "POST"])
def recipe(id):
  comment_form = CommentForm(csrf_enabled=False)
  if comment_form.validate_on_submit():
    new_comment = comment_form.comment.data
    comments[id].append(new_comment)
  return render_template(
    "recipe.html",
    template_recipe=recipes[id],
    template_type=types[id],
    template_description=descriptions[id],
    template_ingredients=ingredients[id],
    template_instructions=instructions[id],
    template_comments=comments[id],
    template_form=comment_form
  )

@app.route('/about')
def about():
  return render_template("about.html")