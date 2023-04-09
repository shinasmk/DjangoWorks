from django.db import models

# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    price = models.FloatField(null=True,blank=True)
    image = models.ImageField(upload_to="images",blank=True)
    follow_author = models.CharField(max_length=2083,blank=True)
    book_available = models.BooleanField()



    def __str__(self) -> str:
        return self.title
