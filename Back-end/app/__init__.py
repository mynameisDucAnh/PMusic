from flask import Flask
from .extensions import db, ma
from .config import Config
from .model import Song, Album, Artist
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
import os
from dotenv import load_dotenv

load_dotenv()

def create_db(app):
    with app.app_context():
        db.create_all()
        print("Database tables created.")

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    ma.init_app(app)
    db.init_app(app)
    create_db(app)
    from .models.songs.controller import songs
    app.register_blueprint(songs)
    
    return app