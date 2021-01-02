# Import modules necessary for app to run
from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField 

# Use Flask framework and configure database, forms for App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:root@35.246.119.161/dnbdatabase"
#external config: mysql+pymysql://root:root@35.246.119.161/dnbdatabase
app.config["SECRET_KEY"] = "bcxvbvcxdfstrqlitjgdsabbxcv"

# Database Reference
db = SQLAlchemy(app)

# Import routes
from application import routes