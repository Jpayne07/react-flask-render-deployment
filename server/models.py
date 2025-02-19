from sqlalchemy import Integer, String, Column
from sqlalchemy.orm import Mapped, mapped_column
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False, )