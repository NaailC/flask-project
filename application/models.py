# Import necessary Modules
from application import db
from datetime import datetime


# Create Artist Class and Table and allow a relationship 
class Artist(db.Model):
    __tablename__= 'artist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(30), nullable=False, unique=True)
    song_name = db.relationship("Songs", backref=db.backref("songs", uselist=False))

# Create Songs Class and Table  
class Songs(db.Model):
    __tablename__= 'songs'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    song_name = db.Column(db.String(60), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    artists = db.relationship("Artist", backref=db.backref("artist", uselist=False))