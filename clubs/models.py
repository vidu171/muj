from django.db import models


class clubs(models.Model):
    clubName = models.CharField(max_length=200)
    clubUserUrl = models.CharField(max_length=200)
    clubLogo = models.CharField(max_length=200)
    clubAdmin = models.CharField(max_length=200)

# Create your models here.
