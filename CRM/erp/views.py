from django.shortcuts import render,redirect
from django.views.generic import View,TemplateView,ListView,DetailView,CreateView,UpdateView
from erp.forms import EmployeeForm,RegistrationForm,LoginForm,BatchForm,StudentProfileForm,UserProfileForm,FacultyProfileForm
from erp.models import Employees,Courses,Batches,StudentProfile,MyUser,FacultyProfile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from erp.forms import CourseForm
from django.urls import reverse_lazy


# Create your views here.
class IndexView(TemplateView):
    template_name="index.html"

class BaseView(TemplateView):
    template_name="base.html"


class EmployeeCreateView(CreateView):
    model=Employees
    form_class=EmployeeForm
    template_name="emp-add.html"
    success_url=reverse_lazy("emp-list")

    # def get(self,request,*args,**kwargs):
    #     form=EmployeeForm
    #     return render(request,"emp-add.html",{"form":form})

    # def post(self,request,*args,**kwargs):
    #     form=EmployeeForm(request.POST,files=request.FILES)

    #     if form.is_valid:
    #         form.save()
    #         # Employees.object.create(**form.cleaned_data)   -----> if its is normal form we need to use this orm query to save data to database
    #         print("data saved")
    #         messages.success(request,'Employee has been created')
    #         return redirect('emp-list')
    #     else:
    #         messages.error(request,"Employee creation failed")
    #         return render(request,"emp-add.html",{"form":form})
        

class EmployeeListView(ListView):
    model=Employees
    context_object_name="employees"
    template_name="emp-list.html"
    # def get(self,request,*args,**kwargs):
    #     qs=Employees.objects.all()
    #     return render(request,'emp-list.html',{'employees':qs})

# localhost:8000/employees/1 
class EmployeeDetailView(DetailView):
    model=Employees
    context_object_name="employee"
    template_name="emp-detail.html"
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     qs=Employees.objects.get(id=id)
    #     return render(request,'emp-detail.html',{'employee':qs})
    
# localhost:8000/employees/remove/1
class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Employees.objects.get(id=id).delete()
        messages.success(request,'deleted successfully')
        return redirect('emp-list')
   
class EmployeeEditView(UpdateView):
    model=Employees
    form_class=EmployeeForm
    template_name="emp-edit.html"
    success_url=reverse_lazy("emp-list")
    
    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     qs=Employees.objects.get(id=id)
    #     form=EmployeeForm(instance=qs)
    #     return render(request,'emp-edit.html',{'form':form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     qs=Employees.objects.get(id=id)
    #     form=EmployeeForm(request.POST,instance=qs,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"Updated")
    #         # Employees.objects.filter(id=id).update(**form.cleaned_data)
    #         return redirect ('emp-list')
    #     else:
    #         messages.error(request,'Updation Failed')
    #         return render(request,'emp-list.html',{'form':form})
        


"""Registration view"""
class RegistratiomView(View):
    def get(self,request,*args,**kwargs):
        form=RegistrationForm
        return render(request,"registration.html",{"form":form})
    def post(self,request,*args,**kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            # form.save()
            User.objects.create_user(**form.cleaned_data)
            messages.success(request,'Registraion Succesfully Done')
            return redirect("home")
        else:
            messages.error(request,'registration error')
            return render(request,"registration.html",{"form":form})


class SignInView(View):
    def get(self,request,*args,**kwargs):
        form=LoginForm()
        return render(request,"login.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")
            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                print(request.user)
                messages.success(request,'login successfull')
                return redirect("home")
            else:
                messages.error(request,'wrong credentials')
                return render(request,'login.html',{"form":form})
            
class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        return redirect('signin')


class EmpHomeView(TemplateView):
    template_name="emp-home.html"


class CourseCreateView(CreateView):
    model=Courses
    form_class=CourseForm
    template_name="course-add.html"
    success_url=reverse_lazy("course-list")
    
    # def get(self,request,*args,**kwargs):
    #     form=CourseForm
    #     return render(request,"course-add.html",{"form":form})
    # def post(self,request,*args,**kwargs):
    #     form=CourseForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request,"Course has been created")
    #         return redirect("course-list")
    #     else:
    #         messages.error(request,"Course creation failed")
    #         return render(request,"course-add.html",{"form":form})
        

class CourseListView(ListView):
    model=Courses
    context_object_name="courses"
    template_name="course-list.html"
    
    # def get(self,request,*args,**kwargs):
    #     qs=Courses.objects.all()
    #     return render(request,"course-list.html",{'courses':qs})
    
class CourseDetailView(DetailView):
    model=Courses
    context_object_name="courses"
    template_name="course-detail.html"

    # def get(self,request,*args,**kwargs):
        # id=kwargs.get('pk')
        # qs=Courses.objects.get(id=id)
        # return render(request,"course-detail.html",{"courses":qs})
        
    
def course_delete_view(request,*args,**kwargs):                #function view --- it us used for small task like delete signout etc....
    id=kwargs.get('pk')
    Courses.objects.get(id=id).delete() 
    return redirect("course-list")           

        # class CourseDeleteView(View):
        #     def get(self,request,*args,**kwargs):
        #         id=kwargs.get('pk')
        #         Courses.objects.get(id=id).delete()
        #         return redirect("course-list")   
    

            
class CourseEditView(UpdateView):
    model=Courses
    form_class=CourseForm
    template_name="course-edit.html"
    success_url=reverse_lazy("course-list")


    # def get(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     qs=Courses.objects.get(id=id)
    #     form=CourseForm(instance=qs)
    #     return render(request,'course-edit.html',{"form":form})
    # def post(self,request,*args,**kwargs):
    #     id=kwargs.get('pk')
    #     qs=Courses.objects.get(id=id)
    #     form=CourseForm(request.POST,instance=qs)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("course-list")
    #     else:
    #         return render(request,'course-edit.html',{"form":form})
    
    
class CourseHomeView(TemplateView):
    template_name="course-home.html"



class BatchCreateView(CreateView,ListView):
    model=Batches
    form_class=BatchForm
    template_name="batch-add.html"
    context_object_name="batches"
    success_url=reverse_lazy("home")


class BatchEditView(UpdateView):
    model=Batches
    form_class=BatchForm
    template_name="batch-edit.html"
    success_url=reverse_lazy("batch-add")

class BatchDetailView(DetailView):     #error error error
    model=Batches
    context_object_name="batches"
    template_name="batch-detail.html"

def batch_delete_view(request,*args,**kwargs):
    id=kwargs.get('pk')
    Batches.objects.get(id=id).delete() 
    return redirect("batch-add")  

class BatchHomeView(TemplateView):
    template_name="batch-home.html"


class StudentHomeView(TemplateView):
    template_name="student-home.html"

class StudentCreateView(View):
    def get(self,request,*args,**kwargs):
        form1=UserProfileForm(initial={"role":"student"})
        form2=StudentProfileForm()
        return render(request,"student-add.html",{"form1":form1,"form2":form2})
    
    def post(self,request,*args,**kwargs):
        form1=UserProfileForm(request.POST)
        form2=StudentProfileForm(request.POST,files=request.FILES)
        if form1.is_valid() and form2.is_valid():
            usr=form1.save()
            form2.instance.user=usr
            form2.save()
            return redirect("home")
        else:
            return render(request,"student-add.html",{"form1":form1,"form2":form2})
        


"""filter"""
from django_filters import FilterSet

class StudentFilter(FilterSet):
    class Meta:
        model=StudentProfile
        fields=["batch","qualification"]



class StudentListView(ListView):
    model=StudentProfile
    template_name="student-list.html"
    context_object_name="students"


    def get(self,request,*args,**kwargs):
        f=StudentFilter(request.GET,queryset=StudentProfile.objects.all())
        print(f.form)
        return render (request,self.template_name,{"filter":f})








class StudentDetailView(DetailView):
    model=StudentProfile
    template_name="student-detail.html"
    context_object_name="students"

# def student_delete_view(request,*args,**kwargs):
#     id=kwargs.get('pk')
#     StudentProfile.objects.get(id=id).delete() 
#     return redirect("student-list")  

        
class StudentDeleteView(View):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        StudentProfile.objects.get(id=id).delete()
        messages.success(request,'deleted successfully')
        return redirect('student-list')
    
       


class StudentEditView(UpdateView):
    model=StudentProfile
    form_class=StudentProfileForm
    template_name="student-edit.html"
    success_url=reverse_lazy("student-list")
           

class BatchEditView(UpdateView):
    model=Batches
    form_class=BatchForm
    template_name="batch-edit.html"
    success_url=reverse_lazy("batch-add")



class FacultyHomeView(TemplateView):
    template_name="faculty-home.html"

class FacultyCreateView(View):
    def get(self,request,*args,**kwargs):
        form1=UserProfileForm(initial={"role":"faculty"})
        form2=FacultyProfileForm()
        return render(request,"faculty-add.html",{"form1":form1,"form2":form2})
    
    def post(self,request,*args,**kwargs):
        form1=UserProfileForm(request.POST)
        form2=FacultyProfileForm(request.POST,files=request.FILES)
        if form1.is_valid() and form2.is_valid():
            usr=form1.save()
            form2.instance.user=usr
            form2.save()
            return redirect("home")
        else:
            return render(request,"faculty-add.html",{"form1":form1,"form2":form2})


class FacultyListView(ListView):
    model=FacultyProfile
    template_name="faculty-list.html"
    context_object_name="faculties"


class FacultyDetailView(DetailView):
    model=FacultyProfile
    template_name="faculty-detail.html"
    context_object_name="faculties"
