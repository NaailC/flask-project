# Import necessary Modules
from application import db
from datetime import datetime

# Join both tables
songartist_table = db.Table('song_artist', db.Model.metadata,
    db.Column('song_id', db.Integer, db.ForeignKey('Songs.song_id')),
    db.Column('artist_id', db.Integer, db.ForeignKey('Artist.artist_id'))
)

# Create Artist Class and Table and allow a relationship 
class Artist(db.Model):
    artist_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(30), nullable=False, unique=True)
    songs = db.relationship("Songs", secondary=songartist_table)

# Create Songs Class and Table  
class Songs(db.Model):
    song_id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    song_name = db.Column(db.String(60), nullable=False)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.artist_id'), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
