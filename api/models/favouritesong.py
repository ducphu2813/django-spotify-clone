from django.db import models

from api.models.song import Song
from api.models.user import User


class FavouriteSong(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    song = models.ForeignKey(Song, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user', 'song')

    def __str__(self):
        return f"{self.user.username} ❤️ {self.song.name}"