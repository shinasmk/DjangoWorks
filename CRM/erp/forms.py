from django import forms

# class EmployeeForm(forms.Form):
#     name=forms.CharField()
#     dept=forms.CharField()
#     salary=forms.IntegerField()
#     gender=forms.CharField()
#     profilepic=forms.ImageField()


from erp.models import Employees,Courses,Batches,StudentProfile,MyUser,FacultyProfile
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm




class EmployeeForm(forms.ModelForm):
    class Meta():
        model=Employees
        exclude=("is_active",)  #another way to create field ,only one field wants to be excluded ,need rest of them at that time we use exclude instead field
        # fields=[
        #     "name",
        #     "dept",
        #     "salary",
        #     "gender",
        #     "profilepic"
        #     ]

        widgets={

            "name":forms.TextInput(attrs={"class":"form-control"}),
            "dept":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-select"}),
            "profilepic":forms.FileInput(attrs={"class":"form-control"})

        }
        

class RegistrationForm(forms.ModelForm):
    class Meta():
        model=User
        fields=[
            "first_name",
            "last_name",
            "username",
            "email",
            "password"
        ]

        widgets={
                "first_name":forms.TextInput(attrs={"class":"form-control"}),
                "last_name":forms.TextInput(attrs={"class":"form-control"}),
                "username":forms.TextInput(attrs={"class":"form-control"}),
                "email":forms.EmailInput(attrs={"class":"form-control"}),
                "password":forms.PasswordInput(attrs={"class":"form-control"})
        }



class LoginForm(forms.Form):
    
    username=forms.CharField()
    password=forms.CharField()

    widgets={
        "username":forms.TextInput(attrs={"class":"form-control"}),
        "password":forms.PasswordInput(attrs={"class":"form-control"})
    }


class CourseForm(forms.ModelForm):
    class Meta():
        model=Courses
        exclude=("is_active",)

        widgets={
            "course_name":forms.TextInput(attrs={"class":"form-control"}),
            "duration":forms.TextInput(attrs={"class":"form-control"}),
            "fees":forms.TextInput(attrs={"class":"form-control"}),
        }

class BatchForm(forms.ModelForm):
    class Meta():
        model=Batches
        exclude=("status","end_date")

        widgets={"batch_name":forms.TextInput(attrs={"class":"form-control"}),
                 "course":forms.Select(attrs={"class":"form-control"}),
                 "start_date":forms.DateInput(attrs={"class":"form-control","type":"date"})

                 
                 

        }
    

class UserProfileForm(UserCreationForm):
    class Meta():
        model=MyUser
        fields=[
            "first_name",
            "last_name",
            "email",
            "username",
            "password1",
            "password2",
            "role",
            "gender",
            "phone_number"
        ]
        widgets={
            "first_name":forms.TextInput(attrs={"class":"form-control"}),
            "last_name":forms.TextInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "username":forms.TextInput(attrs={"class":"form-control"}),
            "password1":forms.PasswordInput(attrs={"class":"form-control"}),
            "password2":forms.PasswordInput(attrs={"class":"form-control"}),
            "role":forms.Select(attrs={"class":"form-control"}),
            "gender":forms.Select(attrs={"class":"form-control"}),
            "phone_number":forms.TextInput(attrs={"class":"form-control"}), 
        }




class StudentProfileForm(forms.ModelForm):
    class Meta():
        model=StudentProfile
        # fields="__all__"    #     __all__   is used to import all fields 
        exclude=("user",)

        widgets={
            "batch":forms.Select(attrs={"class":"form-control"}), 
            "profile_pic":forms.FileInput(attrs={"class":"form-control"}), 
            "qualification":forms.TextInput(attrs={"class":"form-control"})
        }


class FacultyProfileForm(forms.ModelForm):
    class Meta():
        model=FacultyProfile
        # fields="__all__"    #     __all__   is used to import all fields 
        exclude=("user",)

        widgets={
            "batch":forms.Select(attrs={"class":"form-control"}), 
            "profile_pic":forms.FileInput(attrs={"class":"form-control"}), 
            "qualification":forms.TextInput(attrs={"class":"form-control"}),
            "years_of_experience":forms.NumberInput(attrs={"class":"form-control"})
        }

