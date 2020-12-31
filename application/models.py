# Import necessary Modules
from application import db
from datetime import datetime
from sqlalchemy.orm import backref


# Create Artist Class and Table and allow a relationship 
class Artist(db.Model):

    __tablename__ = 'artist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artistname = db.Column(db.String(30), nullable=False, unique=True)
    song = db.relationship('Song', backref='artistsongs', lazy='dynamic')

    
# Create Songs Class and Table  
class Song(db.Model):

    __tablename__ = 'song'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    songname = db.Column(db.String(60), nullable=False)
    dateadded = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    artist = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artistid = db.relationship(Artist)
    