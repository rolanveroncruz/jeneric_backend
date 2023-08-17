from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=512)
    address = models.CharField(max_length=512)
    mobile_number = models.CharField(max_length=16)
    file_location = models.CharField(max_length=1024)