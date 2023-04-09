from django.shortcuts import render,redirect
from django.views.generic import CreateView,TemplateView,FormView,View
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout




from mywebapp.forms import RegistrationForm,LoginForm,VehicleRegistrationForm,VehiclePicForm




from api.models import Vehicles

# Create your views here.


class HomeView(TemplateView):
    template_name="home.html"

class VehicleAddHomeView(TemplateView):
    template_name="vehiclereg.html"

class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy('signin')





class SignInView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            print(uname,pwd)
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect('home')
            else:
                return render(request,self.template_name,{"form":self.form_class})
            


class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')
    

class VehicleAddView(CreateView):
    model=Vehicles
    form_class=VehicleRegistrationForm
    template_name="vehicle-add.html"
    success_url=reverse_lazy("home")
    def form_valid(self,form):
        form.instance.owner=self.request.user
        return super().form_valid(form)
    

# class VehicleAddView(View):
#     def get(self,request,*args,**kwargs):
#         form1=VehicleRegistrationForm()
#         form2=VehiclePicForm()
#         return render(request,"vehicle-add.html",{"form1":form1,"form2":form2})
    
#     def post(self,request,*args,**kwargs):
#         form1=VehicleRegistrationForm(request.POST)
#         form2=VehiclePicForm(request.POST,files=request.FILES)
#         if form1.is_valid() and form2.is_valid():
#             usr=form1.save()
#             form2.instance.user=usr
#             form2.save()
#             return redirect("home")
#         else:
#             return render(request,"vehicle-add.html",{"form1":form1,"form2":form2})