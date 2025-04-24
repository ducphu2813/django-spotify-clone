from django.db import models

from api.models.album import Album
from api.models.song import Song


class AlbumSong(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    pic_url = models.URLField(blank=True, null=True)

    class Meta:
        unique_together = ('album', 'song')

    def __str__(self):
        return f"{self.album.name} - {self.song.name}"