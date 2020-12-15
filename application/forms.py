# Import Form Modules
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError

# Create Form Class to Update Song Name CRUD app 
class SongForm(FlaskForm):
    song_name = StringField('Song Name', validators=[DataRequired()])
    artist_name = StringField('Artist Name', choices=Songs.artist_name validators=[DataRequired()})
    submit = SubmitField('Accept')

class ArtistForm(FlaskForm):
    new_artist_name = StringField('Add Artist Name', validators=[DataRequired()])
    submit = SubmitField('Accept')


