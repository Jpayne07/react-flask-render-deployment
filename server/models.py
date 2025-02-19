from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String, unique = True, nullable = False, )

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    # Convert each user object to a dict
    users_list = [{"id": user.id, "username": user.username} for user in users]
    return jsonify(users_list)