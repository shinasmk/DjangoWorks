from django.db import models

# Create your models here.
class Member(models.Model):
    first_name=models.CharField(max_length=100)
    last_name= models.CharField(max_length=100)
    phone_number=models.IntegerField(null=True)
    joined_date=models.DateField(null=True)
