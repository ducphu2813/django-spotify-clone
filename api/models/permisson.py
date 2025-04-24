from django.db import models

class Permission(models.Model):
    name = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.resource}:{self.action}"