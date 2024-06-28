from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    image_path = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='albums')
    title = models.CharField(max_length=100, null=False, blank=False)
    release_date = models.DateField(blank=True, null=True)
    cover_image = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='songs')
    title = models.CharField(max_length=100, null=False, blank=False)
    duration = models.CharField(max_length=8, blank=True, null=True)  # String to store HH:MM:SS
    file_path = models.CharField(max_length=255, null=False, blank=False)
    image_path = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.title
