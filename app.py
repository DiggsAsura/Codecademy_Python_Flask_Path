# 4. Introduction to Flask
# 1. Introduction to Flask
# 3. Build Your First Flask App
# 6. Review

''' 
Congratulations on building your first Flask app!

You've learned to:

- Import the Flask class and create an application object

from flask import Flask
app = Flask(__name__)

- Define routes for handling requests sent from various URLs

@app.route('/')
def home():
  return '<h1>Hello, World!</h1>'

- Create variable rules to handle dynamic URLs

@app.route('/orders/<user_name>/<int:order_id>')
def orders(user_name, order_id):
  return f'<p>Fetching order #{order_id} for {user_name}.</p>'

Time to put what you've learned to the test!
'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return '<h1>Hello, World!</h1>'

@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
  return f'''
  <h2>Reporter {reporter_id} Bio</h2>
  <a href="/">Return to home page</a>
  '''

@app.route('/article/<article_name>')
def article(article_name):
  return f'''
  <h2>{article_name.replace('-', ' ').title()}</h2>
  <a href="/">Return back to home page</a>
  '''