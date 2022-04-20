# 4. Introduction to Flask
# 1. Introduction to Flask
# 3. Build Your First Flask App
# 4. Render HTML

"""
The response we return from a view function is not limited to plain text or data.
It can also return HTML to be rendered on a webpage:

@app.route('/')
def home():
  return '<h1>Hello, World!</h1>'

We can use triple quotes to contain multi-line code:

@app.route('/')
@app.route('/home')
def home():
  return '''
  <h1>Hello, World!</h1>
  <p>My first paragraph.</p>
  <a href="https://www.codecademy.com">CODECADEMY</a>
  '''
"""

# But question is, do i wanna write HTML inside an python app...? I assume we can
# import the html file and return that instead, or?

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return '''
  <h1>Hello, World!</h1>
  <a href="/reporter">Reporter</a>
  '''
@app.route('/reporter')
def reporter():
  return '''
  <h2>Reporter Bio</h2>
  <a href="/">Return to home page</a>
  '''