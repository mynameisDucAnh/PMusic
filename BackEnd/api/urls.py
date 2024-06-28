from django.urls import path
from . import views

urlpatterns = [
    path("artists/", views.ArtistPostListCreate.as_view(), name="artist-view-create"),
    path("artist/<int:pk>",views.ArtistPostRetrieveUpdateDestrory.as_view(),name="update"),
    path('albums/', views.AlbumPostListCreate.as_view(), name='album-list-create'),
    path('album/<int:pk>/', views.AlbumPostRetrieveUpdateDestroy.as_view(), name='album-retrieve-update-destroy'),
    path('songs/', views.SongPostListCreate.as_view(), name='song-list-create'),
    path('song/<int:pk>/', views.SongPostRetrieveUpdateDestroy.as_view(), name='song-retrieve-update-destroy'),
]
