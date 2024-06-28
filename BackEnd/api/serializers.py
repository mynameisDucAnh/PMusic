from rest_framework import serializers
from .models import Album,Artist,Song

class ArtistPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('id', 'name', 'image_path', 'bio')

class SongPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id', 'album_id', 'title', 'duration', 'file_path', 'image_path')

class AlbumPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'artist_id', 'title', 'release_date', 'cover_image')

