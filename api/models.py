from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=100)
    duration = models.IntegerField()
    artist = models.CharField(max_length=100)

    def __str__(self):
        return self.title


#user model
class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    role = models.ForeignKey('Role', on_delete=models.CASCADE) #đây là khóa ngoại đến bảng Role

    def __str__(self):
        return self.username


#role model
class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#permisson model
class Permission(models.Model):
    name = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)
    action = models.CharField(max_length=100)

    def __str__(self):
        return self.name


#role permission model
class RolePermission(models.Model):
    role = models.ForeignKey('Role', on_delete=models.CASCADE) # khóa ngoại đến bảng Role
    permission = models.ForeignKey('Permission', on_delete=models.CASCADE) # khóa ngoại đến bảng Permission

    class Meta:
        unique_together = ('role', 'permission')  # đảm bảo không trùng lặp

    def __str__(self):
        return self.role.name + ' ' + self.permission.name





