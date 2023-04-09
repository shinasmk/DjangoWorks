from django.db import models

# Create your models here.


class Cakes(models.Model):
    name=models.CharField(max_length=100)
    flavour=models.CharField(max_length=100)
    layer=models.CharField(max_length=100)
    shape=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    weight=models.CharField(max_length=100)
    rating=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

