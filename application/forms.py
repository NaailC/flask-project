# Import Form Modules
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from application.models import Songs, Artist

# Create Form Class to Update Song Name CRUD app 
class SongForm(FlaskForm):
    song_name = StringField('Song Name', validators=[DataRequired()])
    artist_name = SelectField('Artist Name', choices=[(Artist.artist_name)], validators=[DataRequired()})
    submitsong = SubmitField('Accept')

class ArtistForm(FlaskForm):
    new_artist_name = StringField('Add Artist Name', validators=[DataRequired()])
    submitartist = SubmitField('Accept')


