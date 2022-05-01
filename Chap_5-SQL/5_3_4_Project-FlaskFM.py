# 5. Introduction to SQL and Databses for Back-End Web Apps
# 3. Databases in Flask
# 4. Project
# FlaskFM

''' 
You probably often encountered the concept of personalizing your taste in products
online. For example, users create wishlists or shopping lists of various products,
a personal book library as they buy and read books, sewing fabric preferences, or
song library they listen to often. Your personal 'wishlist' is stored in a 
database so you can view it when needed.

In this project, you will create a web service, called FlaskFM, that will allow
users to add songs to their personalized list from a song library curated
by an administrator through a dashboard page. You will model users and playlists
that can be changed by users who add or remove songs. The project work will focus
on the database aspect, but you will create a functional web service for your 
users with us providing you templates, routes, and guidance. Your task will be to
create a database with the schema below:

SONG
id      PRIMARY KEY
title   STRING, INDEXABLE
artist  STRING, INDEXABLE
n       INTEGER

Item
id           PRIMARY KEY
playlist_id  FORIGN KEY
song_id      FOREIGN KEY

Playlist
id  PRIMARY KEY

User
id           PRIMARY KEY
username     STRING, UNIQUE, INDEXABLE
playlist_id  FOREIGN KEY


You will do a simplified version, but imagine users listening to songs on their music
applications and your web service can track which songs/genre they listen to most 
often. Given the collected data, your web app can recommend new music to the users
based on their listening preferences. We will start with the basics, but the sky
is the limit. Let's go.
'''

# app.py

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///song_library.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'you will never guess'
db = SQLAlchemy(app)

@app.route('/')
@app.route('/index')
def greeting():
  return render_template('greeting.html')

@app.errorhandler(404)
def not_found():
  return render_template('404.html')

import routes