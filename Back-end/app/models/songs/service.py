from app.extensions import db
from app.schema import SongSchema
from app.model import Song
from flask import request, jsonify

song_schema = SongSchema()
songs_schema = SongSchema(many=True)

def add_song_service():
    data = request.json
    if data and 'title' in data and 'duration' in data and 'album_id' in data and 'file_path' in data and 'image_path' in data:
        album_id = data['album_id']
        title = data['title']
        duration = data['duration']
        file_path = data['file_path']
        image_path = data['image_path']
    
        try:
            new_song = Song(album_id=album_id, title=title, duration=duration, file_path=file_path, image_path=image_path)
            db.session.add(new_song)
            db.session.commit()
            return jsonify({"message": "Song added successfully"}), 201
        except Exception as e:
            db.session.rollback()
            return jsonify({"error": f"Can't add song. Error: {str(e)}"}), 500
    else:
        return jsonify({"error": "Invalid request. Missing required fields."}), 400

def get_song_by_id_service(id):
    song = Song.query.get(id)
    if song:
        return song_schema.jsonify(song)
    else:
        return jsonify({"error": "Song not found"}), 404
    
def get_all_song_service():
    songs = Song.query.all()
    if songs:
        return songs_schema.jsonify(songs)
    else:
        return jsonify({"error": "Song not found"}), 404
