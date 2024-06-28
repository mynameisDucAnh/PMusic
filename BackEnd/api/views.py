from django.shortcuts import render
from rest_framework import generics,status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Artist,Album,Song
from .serializers import AlbumPostSerializer,ArtistPostSerializer,SongPostSerializer
# Create your views here.

class ArtistPostListCreate(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistPostSerializer

    def delete(self,request,*args,**kwargs):
        Artist.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ArtistPostRetrieveUpdateDestrory(generics.RetrieveUpdateDestroyAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistPostSerializer
    lookup_field = "pk"

class ArtistList(APIView):
    def get(self,request , format = None):
        name = request.query_params.get("name","")
        if name:
            artist = Artist.objects.filter(title_icontains = name)
        else:
            artist = Artist.objects.all()

        serializer = ArtistPostSerializer(artist,MANY=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
class AlbumPostListCreate(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumPostSerializer

class AlbumPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumPostSerializer
    lookup_field = "pk"

class SongPostListCreate(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongPostSerializer

class SongPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongPostSerializer
    lookup_field = "pk"

