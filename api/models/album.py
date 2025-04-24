from django.db import models

from api.models.artist import Artist


class Album(models.Model):
    name = models.CharField(max_length=255)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    image_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name