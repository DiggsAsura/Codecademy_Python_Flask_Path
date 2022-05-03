# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 2. Introduction to Accounts
# 7. Success and Error Handling

'''
As we round things up, it's a good idea to make sure the user experience is 
thoughtful by implementing a way to notify the user when an RSVP succeeds
or if they need to try again in case an error occurs.

Flask provides us with the flash() method to communicate messages powered by
the backend. With flash, Flask can record a message at the end of a request and
access it on the next request only. We can thus use flash to notify users
wheter their important actions succeeed or fail.

Consider the second half of the RSVP route from the previous exercise. We can
update our code to better notify users of what occurs as follows:


# second half of rsvp route
..
  if form.validate_on_submit():
    dinner_party = DinnerParty.query.filter_by(id=in(form.party_id.data)).first()
    # new try block
    try:
      dinner_party.attendees += f', {username}'
      db.session.commit()
      # find the host of dinner_party
      host = User.query.filter_by(id=int(dinner_party.host_id)).first()
      flash(f'You successfully RSVP'd to {host.username}'s dinner party on {dinner_party.date})
      # new except block
    except:
      flash('Please enter a valid Party ID to RSVP!')
  return render_template('rsvp.html', user=user, dinner_parties=dinner_parties, form=form)


- the update to dinner_party.attendees and the commit now occur inside a try 
  block

- the User model is queried for the user hosting dinner_party and stored in
  host
  
- inside the try block, flash() is given a string message as an argument to notify
  the user that an RSVP successfully occured.

- an except block is called when there is an error RSVP'ing

- inside the except block, flash() is given a string message as an argument
  to notify the user that they were not able to RSVP successfully

With the route updated, we can access our flashed messages in a template file
and display them on our page as follows:


{% with messages = get_flashed_messages() %}
  {% if messages %}
    {% for message in messages %}
      {{ message }}
    {% endfor %}
  {% endif %}
{% endwith %}


- the get_flashed_messages() function returns all flashed messages in the last
  session and saves the messages to messages

- if there are any messages, we for loop through each message in messages and 
  display the message {{ message }}

It's best practice to look at your code and evaluate areas where things can go
wrong. When you identify these points, you can utilize flash() to provide 
feedback to the user on what exactly happened and how they can proceed.

'''

# o v e r w h e l m i n g

from app import app, db, login_manager
from flask import request, render_template, flash, redirect, url_for
from models import User, DinnerParty
from flask_login import current_user, login_user, logout_user, login_required
from forms import RegistrationForm, LoginForm, DinnerPartyForm, RsvpForm
from werkzeug.urls import url_parse

# registration route
@app.route('/register', methods=['GET', 'POST'])
def register():
  form = RegistrationForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
  return render_template('register.html', title='Register', form=form)

# user loader
@login_manager.user_loader
def load_user():
  return User.query.get(int(user_id))

# login route
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user and user.check_password(form.password.data):
      login_user(user, remember=form.remember.data)
      next_page = request.args.get('next')
      return redirect(next_page) if next_page else redirect(url_for('index', _external=True, _scheme='https'))
    else:
      return redirect(url_for('login', _external=True, _scheme='https'))
  return render_template('login.html', form=form)

# user route
@app.route('/user/<username>', methods=['GET', 'POST'])
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  dinner_parties = DinnerParty.query.filter_by(party_host_id=user.id)
  if dinner_parties is None:
    dinner_parties = []
  form = DinnerPartyForm(csrf_enabled=False)
  if form.validate_on_submit():
    new_dinner_party = DinnerParty(
      date = form.date.data,
      venue = form.venue.data,
      main_dish = form.main_dish.data,
      number_seats = int(form.number_seats.data),
      party_host_id = user.id,
      attendees = username)
    db.session.add(new_dinner_party)
    db.session.commit()
  return render_template('user.html', user=user, dinner_parties=dinner_parties, form=form)

# rsvp route
@app.route('/user/<username>/rsvp', methods=['GET', 'POST'])
@login_required
def rsvp(username):
  user = User.query.filter_by(username=username).first_or_404()
  dinner_parties = DinnerParty.query.all()
  if dinner_parties is None:
    dinner_parties = []
  form = RsvpForm(csrf_enabled=False)
  if form.validate_on_submit():
    dinner_party = DinnerParty.query.filter_by(int(form.party_id.data)).first()
    # try block
    try:
      dinner_party.attendees += f', {username}'
      db.session.commit()
      # query to find the host of dinner party
      host = User.query.filter_by(id=int(dinner_party.party_host_id)).first()
      # add RSVP success message here:
      flash(f"You successfully RSVP'd to {host.username}'s dinner party on {dinner_party.date}!")
    # except block
    except:
      # add the RSVP failure message here:
      flash("Please enter a valid Party ID to RSVP!")
  return render_template('rsvp.html', user=user, dinner_parties=dinner_parties, form=form)

# landing page route
@app.route('/')
def index():
  current_user = User.query.all()
  return render_template('landing_page.html', current_user=current_user)
