# Import necessary Modules
from application import db
from datetime import datetime
from sqlalchemy.orm import backref


# Create Artist Class and Table and allow a relationship 
class Artist(db.Model):

    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(30), nullable=False, unique=True)

    songs = db.relationship("Song", backref='artist')

# Create Songs Class and Table  
class Song(db.Model):

    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    song_name = db.Column(db.String(60), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    