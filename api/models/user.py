from django.contrib.auth.models import AbstractUser
from django.db import models
# from .role import Role

#user model
class User(AbstractUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    # đây là khóa ngoại đến bảng Role
    role = models.ForeignKey(
        'Role'
        , on_delete=models.CASCADE
        , null=True
    )

    def __str__(self):
        return self.username