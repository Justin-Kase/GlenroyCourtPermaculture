from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse

class Report(models.Model):
    ID = models.AutoField(primary_key=True)
    Temperature_Fahrenheit = models.DecimalField(decimal_places=2,max_digits=6)	
    Relative_Humidity = models.DecimalField(decimal_places=2,max_digits=6)	
    timestamp = models.CharField(max_length=200)
 
    def __str__(self):
        return self.ID 