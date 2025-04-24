from django.db import models

from api.models.user import User


class Playlist(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name