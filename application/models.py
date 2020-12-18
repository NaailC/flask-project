# Import necessary Modules
from application import db
from datetime import datetime


# Create Artist Class and Table and allow a relationship 
class Artist(db.Model):

    __tablename__= 'artists'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    artist_name = db.Column(db.String(30), nullable=False, unique=True)

association_table = db.Table('association_table', db.Model.metadata,
    db.Column('songs_id', db.Integer, db.ForeignKey('songs.id')))
    
# Create Songs Class and Table  
class Songs(db.Model):

    __tablename__= 'songs'
    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    song_name = db.Column(db.String(60), nullable=False)
    date_added = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    