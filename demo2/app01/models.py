from django.db import models

# Create your models here.
#class Group(models.Model):
   # title = models.CharField(max_length=32)
    #mu = models.ForeignKey(to='Menu',default=1)

#class UserInfo(models.Model):
   # name = models.CharField(max_length=32)
    #pwd = models.CharField(max_length=32)
    #group = models.ForeignKey(to="Group")

    #roles = models.ManyToManyField(to="Role")
#class Menu(models.Model):
   # name = models.CharField(max_length=21)

#class Role(models.Model):
#    name = models.CharField(max_length=32)

class Employee(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=256)
    sex=models.CharField(max_length=256)
    age=models.IntegerField(max_length=256)
    hire_date=models.CharField(max_length=256)
    post=models.CharField(max_length=256)
    post_comment=models.CharField(max_length=256)
    salary=models.CharField(max_length=256)
    office=models.IntegerField(max_length=256)
    depart_id=models.IntegerField(max_length=256)
    class Meta:
        db_table='employee'