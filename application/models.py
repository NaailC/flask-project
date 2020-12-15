# Import necessary Modules
from application import db
from datetime import datetime


# Create Artist Class and Table and allow a relationship 
class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(30), nullable=False, unique=True)


# Create Songs Class and Table  
class Songs(db.Model):
    song_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    song_name = db.Column(db.String(60), nullable=False)
    artist_name = db.Column(db.ForeignKey('artist.artist_name'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
