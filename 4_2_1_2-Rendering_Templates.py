# 4. Introduction to Flask
# 2. Jinja2 Templates and Forms
# 1. Flask Templates
# 2. Rendering Templates

'''
Having routes return full web pages as strings is not as realistic way to 
build our site. Containing our HTML in files is the standard and more 
organized approach to structuring our web app.


To work with files, which we will call templates, we use the Flask function
render_template(). Used in the return statement, this function takes a 
template file name as an argument and returns the content to send to the
client. It uses the Jinja2 template engine to generate HTML using the 
template file as blueprint.


return render_template("my_template.html")


To use render_template() in our routes we need to import it from the flask.
A simple app with an index route would look like this:

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
  return render_template("index.html")


Inside the application directory render_template() looks for templates inside
a directory called templates. All template files should be keps inside this
directory. To view the application file structure in this exercise click the 
folder icon in the top left corner of the code editor.
'''

from flask import Flask, render_template
from helper2 import recipes, descriptions, ingredients, instructions

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('4_2_1_2-index.html')

@app.route('/recipe/<int:id>')
def recipe(id):
  return render_template('4_2_1_2-fried_egg.html')

