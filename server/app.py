from flask import Flask, jsonify, send_from_directory
from flask_migrate import Migrate
from sqlalchemy import MetaData
from models import db, User
import os
from dotenv import load_dotenv
load_dotenv()
# create the app
app = Flask(__name__,
            static_url_path='',
    static_folder='../client/dist',
    template_folder='../client/dist')
metadata = MetaData()
app.secret_key = os.environ.get('APP_SECRET_KEY')
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)
db.init_app(app)


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    # Convert each user object to a dict
    users_list = [{"id": user.id, "username": user.username} for user in users]
    return jsonify(users_list)
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve(path):
    target = os.path.join(app.static_folder, path or 'index.html')
    print(f"Trying to serve: {target}")
    if path and os.path.exists(os.path.join(app.static_folder, path)):
        return send_from_directory(app.static_folder, path)
    elif os.path.exists(os.path.join(app.static_folder, 'index.html')):
        return send_from_directory(app.static_folder, 'index.html')
    else:
        return "Not Found", 404
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f"Starting app on port {port}")
    app.run(host='0.0.0.0', port=port, debug=True)

