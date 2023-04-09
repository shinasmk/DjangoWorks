from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,UpdateView,DetailView,View,TemplateView,FormView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.

from.models import Books
from.forms import RegistrationForm,LoginForm



class IndexView(TemplateView):
    template_name="base.html"

class BookListView(ListView):
    model= Books
    context_object_name='books'
    template_name="book-list.html"

class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_url=reverse_lazy("signin")

class SignInView(FormView):
    form_class=LoginForm
    template_name="signin.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")

            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                return redirect("home")
            else:
                return render(request,self.template_name,{"form":self.form_class})
            

class BookDetailView(DetailView):
    model=Books
    context_object_name='books'
    template_name="book-details.html"












class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')

