from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import datetime

# Create your models here.


class AccountInfo(models.Model):
    name = models.CharField(primary_key=True, max_length=256)
    dob = models.DateField()
    ssn = models.IntegerField()
    lang = models.CharField(max_length=64)
    street = models.CharField(max_length=20)
    city= models.CharField(max_length=20)
    state= models.CharField(max_length=20)
    zip= models.IntegerField()
    
    GENDER_CHOICES = ( ('M', 'Male'), ('F', 'Female'),)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="M")
 
    def __unicode__(self):
        return self.name


class Medication(models.Model):
    name = models.CharField(max_length=256)
    dateadded = models.DateField()
    dateupdated = models.DateField()
    dosage = models.CharField(max_length=128)
    frequency = models.CharField(max_length=128)

class BloodWorkType(models.Model):
    B_CHOICES = ( ('WBC', 'WBC'),
                  ('ANC', 'ANC'),
                  ('Hemoglobin', 'Hemo'),
                  ('Platlets', 'Platlets'),
                  ('Calcium', 'Calcium'),
                  )
    type = models.CharField(max_length=32, choices=B_CHOICES, default="WBC")
        

class BloodWork(models.Model):
    name = models.CharField(max_length=256)
    date = models.DateTimeField()
    type = models.ManyToManyField(BloodWorkType)
    reading = models.IntegerField(default="0")
    
    
class Visit(models.Model):
    TYPE_OF_VISIT = ( ('Hospital', 'Hospital'), ('Home', 'Home'),)
    type_of_visit = models.CharField(max_length=32, choices=TYPE_OF_VISIT, default="Hospital")
    visit_time = models.DateTimeField()
    patient = models.ForeignKey(AccountInfo)
    reason_for_visit = models.TextField()
    medications = models.ManyToManyField(Medication)
    bloodwork = models.ForeignKey(BloodWork)
    
    
    