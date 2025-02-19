from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import MetaData
from models import db
# create the app
app = Flask(__name__)
metadata = MetaData()
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)
# initialize the app with the extension
