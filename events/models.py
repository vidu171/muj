from django.db import models
from django.utils import timezone
class events (models.Model):
    club = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    end_time = models.CharField(max_length=200)
    discription = models.TextField()
    poster1 = models.CharField(max_length=400 ,blank=True ,default='')
    poster2 = models.CharField(max_length=400,blank=True ,default='')
    poster3 = models.CharField(max_length=400,blank=True ,default='')
    poster4 = models.CharField(max_length=400,blank=True ,default='')
    video1 = models.CharField(max_length=400,blank=True ,default='')
    video2 = models.CharField(max_length=400,blank=True ,default='')
    person_name_1 = models.CharField(max_length=200)
    person_contact_1=models.CharField(max_length=200)
    person_name_2 = models.CharField(max_length=200)
    person_contact_2 = models.CharField(max_length=200)
    created_date = models.DateTimeField(default= timezone.now())

    def publish(self):
        self.created_date=timezone.now()
        self.save()
    def __str__(self):
        return self.name