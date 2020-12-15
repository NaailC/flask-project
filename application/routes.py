from application import app, db
from application.models import Songs, Artist
from flask import render_template, request, url_for, redirect

# Create a home-page that shows all songs added to the database
@app.route("/")
@app.route("/home")
def home():
    # Find all songs
    all_songs = SongArtist.query.all()
    output = ""
    # Render home html template
    return render_template("home.html", title="Home", all_songs=all_songs)

# Add a song to the database
@app.route("/newsong", methods=['GET','POST'])
def newsong():
# Use Song Form
    form = SongForm()
    # Request POST 
    if request.method == 'POST':
        if form.validate_on_submit():
            # Song form 
            new_song = Songs(song_name=form.song_name.data)
            # Artist form
            artist = Artists(artist_name=form.artist_name.data)
            # Add session to db
            db.session.add(new_song)
            # Commit session to db
            db.session.commit()
            return redirect(url_for("home"))
    # Render add html template 
    return render_template("add.html", title="Add a Song", form=form)

@app.route("/artists", methods=['GET','POST'])
def artists():
    all_artists = Artists.query.all()
    output = ""
    return render_template("artists.html", title="Artists", all_artists=all_artists)

