# Import necessary Modules
from application import db
from datetime import datetime
from sqlalchemy.orm import backref


# Create Artist Class and Table and allow a relationship 
class Artist(db.Model):

    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(30), nullable=False, unique=True)
<<<<<<< HEAD
    songs = db.relationship("Song", backref='artist')

    def __init__(self, artist_name):
        self.artist_name = artist_name

    def __repr__(self):
        return '<Artist %r>' % self.id

=======
    songs = db.relationship('Song', backref='artist', lazy='dynamic')
    justdnb = db.Column(db.Boolean, nullable=False, default=True)
>>>>>>> e9d8ec67c0f5e5207ef94d3cf022cce4e8690533
    
# Create Songs Class and Table  
class Song(db.Model):

    __tablename__ = 'song'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    song_name = db.Column(db.String(60), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
<<<<<<< HEAD
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'))
    artist = db.relationship('movie')
    

    
=======
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    dnb = db.Column(db.Boolean, nullable=False, default=True) 
>>>>>>> e9d8ec67c0f5e5207ef94d3cf022cce4e8690533
