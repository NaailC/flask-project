# Import modules necessary for app to run
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv 


# Use Flask framework and configure database, forms for App
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URI")

#external config: mysql+pymysql://root:root@35.246.119.161/dnbdatabase

app.config["SECRET_KEY"] = getenv("SECRET_KEY")

# Database Reference
db = SQLAlchemy(app)

# Import routes
from application import routes