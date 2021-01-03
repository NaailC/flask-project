import unittest
import pymysql
from flask import url_for
from flask_testing import TestCase

from application import app, db
from application.models import Boxer, Club

class TestBase(TestCase):
    def create_app(self):
        app.config.update(
            SQLALCHEMY_DATABASE_URI="sqlite:///test.db",
            SECRET_KEY='TEST_SECRET_KEY',
            DEBUG=True
        )
        return app

    def setupartist(self):
        db.create_all()
        test_artist = Artist(artistname = "TestArtist")
        db.session.add(test_artist)
        db.session.commit()

    def setupsong(self):
        test_song = Song(songname = "TestSong", artist=1)
        db.session.add(test_boxer)
        db.session.commit()

    def teardown(self):
        db.session.remove()
        db.drop_all()


class TestViews(TestBase):
    def test_home_get(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_newsong_get(self):
        response = self.client.get(url_for('newsong'),follow_redirects=True)
        self.assertEqual(response.status_code, 200)
   
    def test_club_get(self):
        response = self.client.get(url_for('newartist'), follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
    def test_update_get(self):
        response = self.client.get(url_for('update', song_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_get(self):
        response = self.client.get(url_for('delete', song_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_deleteclub_get(self):
        response = self.client.get(url_for('deleteartist', artist_id=1), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_ArtistSong(self):
        response = self.client.get(url_for("home"))
        self.assertNotIn(b"Test the flask app", response.data)

class TestCreate(TestBase):
    def test_artist(self):
        response = self.client.post(
            url_for("newartist"),
            data=[(artistname = "TestArtist2"), follow_redirects=True]
        self.assertNotIn(b"TestSong", response.data)
    
    
    def test_addboxer(self):
        response = self.client.post(
            url_for("addboxer"),
            data=[(firstname = TestSong2, artist=1), follow_redirects=True]
            follow_redirects=True
        )
        self.assertNotIn(b"Create a new boxer", response.data)

class TestUpdate(TestBase):
    def test_update_boxer(self):
        response = self.client.post(
            url_for("update", boxer_id=1),
            data=dict(firstname = "Test the firstname", lastname= "test the lastname", email= "test the boxer email", weightclass="Test the weighclass"),
            follow_redirects=True
        )
        self.assertIn(b"not found", response.data)

class TestDelete(TestBase):
    def test_delete_boxerclub(self):
        response = self.client.get(
            url_for("delete", boxer_id=1),
            follow_redirects=True
        )
        self.assertIn(b"not found", response.data)


    def test_delete_club(self):
        response = self.client.get(
            url_for("deleteclub", club_id=1),
            follow_redirects=True
        )
        self.assertNotIn(b"not found", response.data)