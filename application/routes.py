from application import app, db
from application.models import Song, Artist
from application.forms import SongForm, ArtistForm
from flask import render_template, request, url_for, redirect

# Create a home-page that shows all songs added to the database
@app.route("/", methods=['GET'])
@app.route("/home", methods=['GET'])
def home():
    # Find all songs
    artist = Artist.query.all()
    print(artist)
    # Render home html template
    return render_template("home.html", title="Home", artist=artist)

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

@app.route("/justdnb/<int:id>")
def justdnb(id):
    Artist = Artist.query.filter_by(id=id).first()
    artist.justdnb = False
    db.session.commit()
    return f"Artist {artist_name} makes more than DnB."

# Update the artist
@app.route("/update/<int:id>", methods=['GET', 'POST'])
def update(id):
    form = ArtistForm()
    updateartist = Artist.query.filter_by(id=id).first()
    if request.method == 'POST':
        artist.artist_name = form.artist_name.data
        db.session.commit()
        return redirect(url_for("home"))

# Delete the song 
@app.route("/delete/<int:id>", methods=['GET','POST'])
def delete(id):
    deletesong = Songs.query.filter_by(id=id).first()
    db.session.delete(deletesong)
    db.session.commit()
    return redirect(url_for("home"))