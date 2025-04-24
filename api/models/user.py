from django.db import models
# from .role import Role

#user model
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    # đây là khóa ngoại đến bảng Role
    role = models.ForeignKey(
        'Role'
        , on_delete=models.CASCADE
    )

    def __str__(self):
        return self.username