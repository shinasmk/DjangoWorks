from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.name





class Vehicles(models.Model):
    name=models.CharField(max_length=200)
    model=models.CharField(max_length=200)
    number=models.CharField(max_length=200)
    km_driven=models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    options=(
        ('petrol','petrol'),
        ('diesel','diesel'),
        ('ev','ev'),
        ('cng','cng')
             )
    fuel_type=models.CharField(max_length=200,choices=options,default='petrol')
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    condition=models.CharField(max_length=200)
    date_of_purchase=models.CharField(max_length=200)
    owner_type=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    options=(
        ('available','available'),
        ('sold','sold'),
             )
    status=models.CharField(max_length=200,choices=options,default='available')
    phone_number=models.CharField(max_length=100)
    price=models.PositiveIntegerField(default=10000)

    def __str__(self):
        return self.name
    
    @property
    def vehicle_images(self):
        return VehiclePics.objects.filter(vehicle=self)
    
    @property
    def querys(self):
        return Questions.objects.filter(add=self)
    


class VehiclePics(models.Model):
    vehicle=models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    images=models.ImageField(upload_to="images",null=True)

class Wishlist(models.Model):
    vehicle=models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)

class Questions(models.Model):
    question=models.CharField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    add=models.ForeignKey(Vehicles,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
     
    def __str__(self) -> str:
        return self.question
    
    @property
    def question_answer(self):
        return Answers.objects.filter(question=self)
    
class Answers(models.Model):
    answer=models.CharField(max_length=200)
    ownwer=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now_add=True)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.answer
    
    