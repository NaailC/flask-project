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
        db.session.add(test_songr)
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
    def test_read_artist(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"TestArtist", response.data)

    def test_read_song(self):
        response = self.client.get(url_for("home"))
        self.assertIn(b"TestSong", response.data)

class TestCreate(TestBase):
    def test_artist(self):
        response = self.client.post(
            url_for("newartist"),
            data=[(artistname = "TestArtist"), follow_redirects=True]
        self.assertNotIn(b"TestArtist", response.data)
    
    
    def test_addsong(self):
        response = self.client.post(
            url_for("newsong"),
            data=[(songname = TestSong2, artist=1), follow_redirects=True]
            follow_redirects=True
        )
        self.assertIn(b"Add a Song", response.data)

class Test_Update(TestBase):
    def test_update_song(self):
        response = self.client.post(
            url_for("update", id=1),
            data=[(songname = "TestUpdateSong")],
            follow_redirects=True
        )
        self.assertIn(b"Home", response.data)

class Test_Delete(TestBase):
    def test_delete_song(self):
        response = self.client.get(
            url_for("delete", id=1),
            follow_redirects=True
        )
        self.assertIn(b"Home", response.data)


    def test_delete_artist(self):
        response = self.client.get(
            url_for("deleteartist", id=1),
            follow_redirects=True
        )
        self.assertIn(b"Home", response.data)