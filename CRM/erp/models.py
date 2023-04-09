from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=100)
    dept=models.CharField(max_length=100)
    salary=models.PositiveIntegerField()
    options=(("female","female"),("male","male"))
    gender=models.CharField(max_length=100,choices=options)
    is_active=models.BooleanField(default=True)
    profilepic=models.ImageField(upload_to="images",null=True,blank=True)

    def __str__(self):
        return self.name
    
class Courses(models.Model):
    course_name=models.CharField(max_length=200,unique=True)
    duration=models.CharField(max_length=200)
    fees=models.PositiveIntegerField()
    is_active=models.BooleanField(default=True)

    def __str__(self):
        return self.course_name



class Batches(models.Model):
    batch_name=models.CharField(max_length=100)
    course=models.ForeignKey(Courses,on_delete=models.CASCADE)
    options=(
        ("yet_to_begin","yet_to_begin"),
        ("ongoing","ongoing"),
        ("completed","completed")
    )
    status=models.CharField(max_length=100,choices=options,default="yet_to_begin")
    start_date=models.DateField(null=True)
    end_date=models.DateField(null=True)

    def __str__(self):
        return self.batch_name
    


class MyUser(AbstractUser):
    phone_number=models.CharField(max_length=100)
    options=(("hr","hr"),
            ("counsellers","counsellers"),
            ("faculty","faculty"),
            ("admin","admin"),
            ("student","student"),
            ("manager","manager")
    )
    role=models.CharField(max_length=100,choices=options,default="admin")
    opt=(
        ("male","male"),
        ("female","female")
    )
    gender=models.CharField(max_length=100,choices=opt,default="male")


class StudentProfile(models.Model):
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batches,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="student_images",null=True,blank=True)
    qualification=models.CharField(max_length=200)

class FacultyProfile(models.Model):
    user=models.OneToOneField(MyUser,on_delete=models.CASCADE)
    batch=models.ForeignKey(Batches,on_delete=models.CASCADE)
    profile_pic=models.ImageField(upload_to="faculty_images",null=True,blank=True)
    qualification=models.CharField(max_length=100)
    years_of_experience=models.PositiveIntegerField()
