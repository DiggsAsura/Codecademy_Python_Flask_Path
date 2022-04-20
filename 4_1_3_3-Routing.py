# 4. Introduction to Flask
# 1. Introduction to Flask
# 3. Build Your First Flask App
# 3. Routing

'''
Each time we visit a URL in a browser, it makes a request to the web server, which
processes the request and returns a response back to the browser. In our Flask
app, we can create endpoints to handle the various requests. Requests from different
URLs can be directed to different endpoints in a process called routing.

To build a route, we need to first define a function, known as a view function,
that contains the code for processing the request and generating a response.
The response could be something as simple as a string of text. Then, we can use
the route() decorator to bind a URL to the view function such that the function
will be triggered when the URL is visited:

@app.route('/')
def home()
  return 'Hello, World!'

The route() decorator takes the URL path as parameter, or the part of the URL 
that follows the domain name. All URL paths must start with a leading slash. In
the above example, if we visit http://localhost:5000/ in the browser, 
Hello, World! will be displayed on the webpage. 

Multiple URLs can also be bound to the same view function:

@app.route('/')
@app.route('/home')
def home():
  return 'Hello, World!'

Now, both http://localhost:5000 and http://localhost:5000/home will display 
Hello, World!
'''

# I first tried to put @app.route('/reporter') with the two others, but that ofc did not work out!
# Forgot and got reminded how @decorators work, they have to be directly above their function they
# decorate :)

from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
  return 'Hello, World!'

@app.route('/reporter')
def reporter():
  return 'Reporter Bio'

