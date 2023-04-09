from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Vehicles(models.Model):
    vehicle_name=models.CharField(max_length=100)
    vehicle_number=models.CharField(max_length=100)
    vehicle_model=models.PositiveIntegerField()
    owner=models.CharField(max_length=100)
    km_driven=models.PositiveIntegerField()
    date_of_purchase=models.DateField()
    options=(("petrol","petrol"),("diesel","diesel"),("ev","ev"))
    fuel_type=models.CharField(max_length=100,choices=options)