# 4. Introduction to Flask
# 1. Introduction to Flask
# 3. Build Your First Flask App
# 5. Variable Rules

''' 
We've seen how the route() decorator can be used to bind one or more static URLs
to a view function. But what if we want to handle a set of URLs that may be 
constantly changing? Let's take a look at how we can use variable rules to allow 
for dynamic URLs.

When specifying the URL to bind to a view function, we have the option of making
any section of the path between the slashes (/) variable by indicating 
<variable_name>. These variable parts will then be passed to the view function
as arguments. For example:

@app.route('/orders/<user_name>/<int:order_id>'):
  return f'<p>Fetching order #{order_id} for {user_name}.</p>'

Now, URLs like '/orders/john/1' and '/orders/jane/8' can all be handled by the
orders() function.

Note that we can also optionally enforce the type of the variable being accepted
using the syntax <converter:variable_name>. The possible converter types are:

string  | accepts any text without a slash (default)
int     | accepts positive integers
float   | accepts positive floating point values
path    | like string but also accepts flashes
uuid    | accepts UUID strings

'''

from flask import Flask
import random
app = Flask(__name__)

my_rng = random.randint(1, 3000)

@app.route('/')
@app.route('/home')
def home():
  return f'''
  <h1>Hello, World!</h1>
  <a href="/reporter/{my_rng}">Reporter</a>
  '''

@app.route('/reporter/<int:reporter_id>')
def reporter(reporter_id):
  return f'''
  <h2>Reporter {reporter_id} Bio</h2>
  <a href="/">Return to home page</a>
  '''
           