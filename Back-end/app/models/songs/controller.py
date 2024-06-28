from flask import Blueprint
from .service import add_song_service, get_song_by_id_service,get_all_song_service

songs = Blueprint("songs", __name__)


@songs.route("/song-manage/song", methods=['POST'])
def add_song():
    return add_song_service()

@songs.route("/song-manage/song/<int:id>", methods=['GET'])
def get_song_by_id(id):
    return get_song_by_id_service(id)

@songs.route("/song-manage/songs", methods=['GET'])
def get_all_song():
    return get_all_song_service()
