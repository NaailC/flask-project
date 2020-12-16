import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Songs, Artist

# Set test variables for test admin user
test_admin_first_name = "Naail"
test_admin_last_name = "Choudhury"
test_admin_email = "naailchoudhury@gmail.com"
test_admin_password = "bigdog"

class TestViews(TestBase):
#TEST JENKINS SERVER
    def test_home_get(self):

        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)