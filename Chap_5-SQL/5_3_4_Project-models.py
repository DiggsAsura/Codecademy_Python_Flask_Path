# 5_3_4_Project
# models.py

from app import app, db

#the User model: each user has a username, and a playlist_id foreign key referring
# to the user's Playlist
class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), index=True, unique=True)
  playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
  
  def __repf__(self):
    return f'{self.username}'

#create the Song model here + add a nice representation method
class Song(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), index=True, unique=False)
  artist = db.Column(db.String(100), index=True, unique=False)
  n = db.Column(db.Integer, index=False, unique=False)
  
  def __repr__(self):
    return f'{self.title} by {self.artist}'


#create the Item model here + add a nice representation method
class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  song_id = db.Column(db.Integer, db.ForeignKey('song.id'))
  playlist_id = db.Column(db.Integer, db.ForeignKey('playlist.id'))
  
  def __repr__(self):
    return f'{song_id} in {playlist_id}'


class Playlist(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  items = db.relationship('Item', backref='playlist', lazy='dynamic', cascade='all, delete, delete-orphan')
