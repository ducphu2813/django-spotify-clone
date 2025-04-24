from django.db import models

#artist model
class Artist(models.Model):
    name = models.CharField(max_length=100)
    picture = models.URLField()
    # đây là khóa ngoại đến bảng Role
    user = models.ForeignKey(
        'User'
        , on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name