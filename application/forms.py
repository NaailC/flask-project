# Import Form Modules
from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, ValidationError
from application.models import Song, Artist

# Create Form Class to Update Song Name CRUD app 
class SongForm(FlaskForm):
    songname = StringField('Song Name', validators=[DataRequired()])
    artistname = SelectField('Artist Name', choices=[('Artist.artistname')], validators=[DataRequired()])
    submitsong = SubmitField('Accept')

class ArtistForm(FlaskForm):
    artist_name = StringField('Add Artist', validators=[DataRequired()])
    submitartist = SubmitField('Accept')


