from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from api.models import Vehicles,VehiclePics







class RegistrationForm(UserCreationForm):
    class Meta():
        model=User
        fields=[
            "username",
            "email",
            "password1",
            "password2"
        ]

        widgets={
                "username":forms.TextInput(attrs={"class":"form-control"}),
                "email":forms.EmailInput(attrs={"class":"form-control"}),
                "password":forms.PasswordInput(attrs={"class":"form-control"})
        }
    



class LoginForm(forms.Form):
    
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class VehicleRegistrationForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields=[
            "name",
            "model",
            "number",
            "km_driven",
            "category",
            "fuel_type",
            "condition",
            "date_of_purchase",
            "owner_type",
            "location",
            "status",
            "phone_number",
            "price",

        ]

    

class VehiclePicForm(forms.ModelForm):
    class Meta:
        model=VehiclePics
        fields="__all__"
   