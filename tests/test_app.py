import unittest
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Song, Artist

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True
        )
        return app

    def setUp(self):

        db.create_all()
        test_artist = Artist(artistname="TestArtist")
        db.session.add(test_artist)
        db.session.commit()
        test_song = Song(songname="TestSong", artist=1)
        db.session.add(test_song)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_newsong_get(self):
        response = self.client.get(url_for('newsong'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
   
    def test_artist_get(self):
        response = self.client.get(url_for('newartist'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_deletesong_get(self):
        response = self.client.get(url_for('delete', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_deleteartist_get(self):
        response = self.client.get(url_for('deleteartist', id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 302)

class TestRead(TestBase):
    def test_read_artist(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"TestArtist", response.data)

    def test_read_song(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"TestSong", response.data)

class TestCreate(TestBase):
    def test_read_artist(self):
        response = self.client.post(url_for("newartist"),
            data=dict(artistname = "TestArtist2"), 
            follow_redirects=True)
        self.assertIn(b"TestArtist2", response.data)
    
    
    def test_addsong(self):
        response = self.client.post(url_for("newsong"),
            data=dict(songname="TestSong2", artist=1),
            follow_redirects=True)
        self.assertIn(b"TestSong2", response.data)

class TestUpdate(TestBase):
    def test_update_song(self):
        response = self.client.post(url_for("update", id=1),
            data=dict(songname="TestUpdateSong", artistname=1),
            follow_redirects=True)
        self.assertIn(b"TestUpdateSong", response.data)

class TestDelete(TestBase):
    def test_delete_song(self):
        response = self.client.get(url_for("delete", id=1),
            follow_redirects=True)
        self.assertNotIn(b"TestSong", response.data)


    def test_delete_artist(self):
        response = self.client.get(
            url_for("deleteartist", id=1),
            follow_redirects=True)
        self.assertNotIn(b"TestArtist", response.data)