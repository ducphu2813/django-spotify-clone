from django.db import models


#role model
class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
