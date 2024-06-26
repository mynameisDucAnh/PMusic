from flask import Blueprint

songs = Blueprint("songs",__name__)
@songs.route("/get-all-songs")
def get_all_songs():
    return "All song"