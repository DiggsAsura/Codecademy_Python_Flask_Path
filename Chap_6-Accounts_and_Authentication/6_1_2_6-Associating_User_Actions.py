# 6. Advanced Flask Functionality
# 1. Accounts and Authentication
# 2. Introduction to Accounts
# 6. Associating User Actions

'''
Our users are now able to create accounts and log in. You may be curious, and 
ask yourself. "How can I make sure that they manipulate only their data and not 
someone else's?"

We solve this association problem by making every dinner party an instance of a
DinnerParty model, where each party is created by an instance of the User model.
We can then use the unique identifying attributes of each object to ensure
functionality like creating new dinner parties hosted by a specific user and 
letting users RSVP to specific dinner party.

We can update our user endpoint with functionality to check for existing dinner
parties and create a new dinner party using a form:


def user(username):
  user = User.query.filter_by(username=username).first_or_404()
  dinner_parties = DinnerParty.query.filter_by(party_host_id=user.id)
  if dinner_parties is None:
    dinner_parties = []
  form = DinnerPartyForm(csrf_enabled=False)


- query the DinnerParty model for all dinner parties where the party host is our
  logged-in user, and store the parties in dinner_parties

- if there is no dinner party hosted by the logged-in user, set dinner_parties
  to an empty list

- create a DinnerPartyForm named form

Once the user submits the form fro a new dinner party, we can use the form data
to create a new DinnerParty instance:


# user route continued
... 
  if form.validate_on_submit():
    new_dinner_party = DinnerParty(date=form.date.data, venue=form.venue.data, main_dish=form.main_dish.data, number_seats=ing(form.number_seats.data), party_host_id=user.id, attendees=username)
    db.session.add(new_dinner_party)
    db.session.commit()
  return render_template('user.html', user=user, dinner_parties=dinner_parties, form=form) 



- if form validates, create a new DinnerParty object new_dinner_party

- the DinnerParty attributes (date, venue....., attendees) are assigned values from
  their accompanying form field data

- the attendees attribute is initialized with the logged-in user's username

- new_dinner_party is added to the session and commited

We can create a new route that will allow users to see all the dinner parties
that are happening and provided a form for RSVPing to a specific party:


def rsvp(username):
  user = User.query.filter_by(username=username).first_or_404()
  dinner_parties = DinnerParty.query.all()
  if dinner_parties is None:
    dinner_parties = []
  form = RsvpForm(csrf_enabled=False)
  if form.validate_on_submit():
    dinner_party = DinnerParty.query.filter_by(id=int(form.party_id.data)).first()
    dinner_party.attendees += f", {username}"
    db.session.commit()
  return render_template('rsvp.html', user=user, dinner_parties=dinner_parties, form=form)


- set user to be logged-in user

- query all dinner parties in the DinnerParty model and save them to 
  dinner_parties for display on the page

- create an RSVP form named form

- if form validates, query the DinnerParty model for the dinner party with an id
  that matches the id entered in the form

- update the attendee list with the logged-in user's username and commit the
  change


'''


from app import app, db, login_manager
from flask import request, render_template, flash, redirect, url_for
from models import User, DinnerParty
from flask_login import current_user, login_user, logout_user, login_required
from forms import RegistrationForm, LoginForm, DinnerPartyForm, RsvpForm
from werkzeug.urls import url_parse

# registration route
@app.route('/regist', methods=['GET', 'POST'])
def register():
  form = RegistrationForm(csrf_enabled=False)
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
  return render_template('register.html', title='Register', form=form)

# user loader
@login_manager
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
  if form.validate_on_submit():
    # update the values of each attribute to the corresponding form data here:
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
@app.route('/user/<username>/rsvp/', methods=['GET', 'POST'])
@login_required
def rsvp(username):
  user = User.query.filter_by(username=username).first_or_404()
  dinner_parties = DinnerParty.query.all()
  if dinner_parties is None:
    dinner_parties = []
  form = RsvpForm(csrf_enabled=False)
  if form.validate_on_submit():
    # query the DinnerParty model here:
    dinner_party = DinnerParty.query.filter_by(id=int(form.party_id.data)).first()
    # update the attendees here:
    dinner_party.attendees += f', {username}'
    db.session.commit()
  return render_template('rsvp.html', user=user, dinner_parties=dinner_parties, form=form)

# landing page route
@app.route('/')
def index():
  # grab all guests and display them
  current_user = User.query.all()
  return render_template('landing_page.html', current_users = current_users)