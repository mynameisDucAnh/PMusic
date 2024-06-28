from .extensions import ma
from .model import Song, Album, Artist

class SongSchema(ma.Schema):
    class Meta:
        model = Song
        fields = ('id', 'album_id', 'title', 'duration', 'file_path', 'image_path')

class AlbumSchema(ma.Schema):
    class Meta:
        model = Album
        fields = ('id', 'artist_id', 'title', 'release_date', 'cover_image')

class ArtistSchema(ma.Schema):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'image_path', 'bio')