# Import necessary Modules
from application import db
from datetime import datetime
from sqlalchemy.orm import backref


# Create Artist Class and Table and allow a relationship 
class Artist(db.Model):

    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(30), nullable=False, unique=True)

    tunes = db.relationship("Song", backref='artist')

    def __init__(self, artist_name):
        self.artist_name = artist_name

    def __repr__(self):
        return '<Artist %r>' % self.id

    
# Create Songs Class and Table  
class Song(db.Model):

    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    song_name = db.Column(db.String(60), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'))
    artist = db.relationship('movie')
    
    def __init__(self, song_name):
        self.song_name = song_name
        self.artist = artist

    def __repr__(self):
        return '<Song %r>' % self.id