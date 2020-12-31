from application import app, db
from application.models import Song, Artist
from application.forms import SongForm, ArtistForm
from flask import render_template, request, url_for, redirect

# Create a home-page that shows all songs added to the database
@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    # Find all songs
    all_songs = Song.query.all()
    # Render home html template
    return render_template("home.html", title="Home", all_songs='all_songs')

@app.route("/artist", methods=['GET'])
def artists():
    # Find all songs
    all_artists = Artist.query.all()
    # Render home html template
    return render_template("artists.html", title="Artists", all_artists='all_artists')

# Add a song to the database
@app.route("/newsong", methods=['GET','POST'])
def newsong():
# Use Song Form
    form = SongForm()
    # Request POST 
    if request.method == 'POST':
        if form.validate_on_submit():
            new_song = Songs(form.song_name.data, form.artist_name.data)
            # Add + Commit session to db
            db.session.add(new_song)
            db.session.commit()
            return redirect(url_for("home"))
    # Render add html template 
    return render_template("newsong.html", title="Add a Song", form=form)

# Add an artist to the database
@app.route("/newartist", methods=['GET','POST'])
def newartist():
    form = ArtistForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            new_artist = Artist(artist_name=form.artist_name.data)
            db.session.add(new_artist)
            db.session.commit()
            return redirect(url_for("home"))
    
    return render_template("newartist.html", title="Add an Artists", form=form)

# Update the song
@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    form = SongForm()
    updateartist = Song.query.filter_by(id=id).first()
    if request.method == 'POST':
        song.song_name = form.song_name.data
        db.session.commit()
        return redirect(url_for("home"))

# Delete the song 
@app.route("/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    deletesong = Songs.query.filter_by(id=id).first()
    db.session.delete(deletesong)
    db.session.commit()
    return redirect(url_for("home"))