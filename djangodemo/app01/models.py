
from django.db import models

# Create your models here.
# class UserInfo (models.Model):
#     username = models.CharField(max_length=32)
#     email = models.EmailField(max_length=32)
#     ut = models.ForeignKey("UserType")
#
# class UserType (models.Model):
#     title = models.CharField(max_length=32)
#     roles = models.ManyToManyField(to="Roles")
#     def __str__(self):
#         return self.title
#
# class Roles(models.Model):
#     caption = models.CharField(max_length=32)
#     def __str__(self):
#         return self.caption
class UserInfo(models.Model):
    pass