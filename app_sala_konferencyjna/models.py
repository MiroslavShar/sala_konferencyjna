from django.db import models

# Create your models here.

class Hall(models.Model):
    name_hall = models.CharField(max_length=255)
    capacity_hall = models.IntegerField
    availability_of_projector = models.BooleanField(default=True)
