# video_hosting/models.py

from django.db import models

class Video(models.Model):
    img = models.ImageField(upload_to='img/')
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/')

class Audio(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audios/')
