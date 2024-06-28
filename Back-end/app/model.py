from app.extensions import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image_path = db.Column(db.String(255), nullable=True)
    bio = db.Column(db.Text, nullable=True)

    def __init__(self, name, bio=None, image_path=None):
        self.name = name
        self.image_path = image_path
        self.bio = bio

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    release_date = db.Column(db.Date, nullable=True)
    cover_image = db.Column(db.String(255), nullable=True)
    artist = db.relationship('Artist', backref=db.backref('albums', lazy=True))

    def __init__(self, artist_id, title, release_date=None, cover_image=None):
        self.artist_id = artist_id
        self.title = title
        self.release_date = release_date
        self.cover_image = cover_image

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    duration = db.Column(db.String(8), nullable=True)  # String to store HH:MM:SS
    file_path = db.Column(db.String(255), nullable=False)
    image_path = db.Column(db.String(255), nullable=True)
    album = db.relationship('Album', backref=db.backref('songs', lazy=True))

    def __init__(self, album_id, title, duration=None, file_path=None, image_path=None):
        self.album_id = album_id
        self.title = title
