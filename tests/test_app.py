import unittest
import pymysql
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

    def setupartist(self):
        db.create_all()
        test_artist = Artist(artistname = "TestArtist")
        db.session.add(test_artist)
        db.session.commit()

    def setupsong(self):
        test_song = Song(songname = "TestSong", artist=1)
        db.session.add(test_boxer)
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
   
    def test_club_get(self):
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
        self.assertEqual(response.status_code, 200)

class TestRead(TestBase):
    def test_read_Artist(self):
        response = self.client.get(url_for("home"))
        self.assertNotIn(b"TestArtist", response.data)

    def test_read_Song(self):
        response = self.client.get(url_for("home"))
        self.assertNotIn(b"TestSong", response.data)

class TestCreate(TestBase):
    def test_artist(self):
        response = self.client.post(
            url_for("newartist"),
            data=[(artistname = "TestArtist2"), follow_redirects=True]
        self.assertNotIn(b"TestSong", response.data)