from django.db import models

class user(models.Model):
    Name = models.CharField(max_length=200)
    regNo = models.CharField(max_length=200)
    clubName1 = models.CharField(max_length=200 ,blank=True ,default='')
    clubName2 = models.CharField(max_length=200 ,blank=True ,default='')
    clubName3 = models.CharField(max_length=200 ,blank=True ,default='')
    clubName4 = models.CharField(max_length=200 ,blank=True ,default='')
# Create your models here.
