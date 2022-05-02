# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 2. Introduction to Accounts
# 5. Login in with Flask

'''
We currently have a working form grabbing user data and signing them up to our
application. Good work! Next, let's allow users to login by using a Flask-Login
object called LoginManager().


login_manager = LoginManager()
login_manager.init_app(app)


- here we create a LoginManager object and initialize it with the init_app()
  method and our application object app

Flask-Login provides us with a helpful decorator that we'll place on endpoints
we want to be protected. Remember, decorators allow us to run bits of code 
before ultimately running a function or in this case our flask endpoint.


@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  return render_template('user.html', user=user)


- the @login_required decorator is used to protect the user route

- the User table is queried for a user that matches the provided username

We will use this decorator on every Flask endpoint that we want only accessible by
logged in users. This will check to make sure the user login is still stored in
memory. So long as the user memory has not been cleared with a logout or browser
refreshing clear, the LoginManager() will be able to retrieve the identity of
the user before allowing them to access the information on that page.

We also need an additional helper function to load our individual user when 
trying to access protected routes.


@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))


- the load user() function loads a user with a given user_id

We can then login a user with a login route, paired with a login form, as shown
below:


@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.check_password(form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page)
  if next_page else redirect(url_for('index', _external=True, _scheme='https')):
    else:
      return redirect(url_for('login', _external=True, _scheme='https'))
  return render_template('login.html', form=form)


- initialize a Loginform form

- if the form validates, query the User table for the user with an email that 
  matches the provided email

- if a user is found, user.check_password(form.password.data) checks the form
  entered password against the user's password

- if there is a match, login_user() logs user in and redirects to either
  next_page or the index route

- if no user is found or the password does not match, we redirect to the login
  route

'''

