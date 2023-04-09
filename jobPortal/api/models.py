from django.db import models

# Create your models here.


class Jobs(models.Model):
    company=models.CharField(max_length=200)
    role=models.CharField(max_length=200)
    experience=models.PositiveIntegerField()
    slots=models.CharField(max_length=200)
    qualification=models.CharField(max_length=200)
 

    def _str_(self) -> str:
        return self.company


class Companies(models.Model):
    company_name=models.CharField(max_length=100)
    services=models.CharField(max_length=100)
    description=models.CharField(max_length=100)

    def __str__(self):
        return self.company_name
