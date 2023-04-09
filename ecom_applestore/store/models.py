from django.db import models

# Create your models here.


class Products(models.Model):
    productname = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True,blank=True)
    image_url = models.CharField(max_length=2083,blank=True)
    product_available = models.BooleanField()


    def __str__(self) -> str:
        return self.productname
    


    
