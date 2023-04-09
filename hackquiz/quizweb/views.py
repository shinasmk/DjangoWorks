from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.views.generic import CreateView,View,FormView,TemplateView,ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages

import random


from quizweb.forms import RegistrationForm,LoginForm


from quiz.models import Category,Questions,QuizRecord

# Create your views here.

class IndexView(TemplateView):
    template_name="home.html"
    

class SignUpView(CreateView):
    model=User
    form_class=RegistrationForm
    template_name="register.html"
    success_message='Registration has been Successfull'
    success_url=reverse_lazy("signin")

    def form_valid(self,form):
        messages.success(self.request,"Account has been created")
        return super().form_valid(form)
    def form_invalid(self,form):
        messages.error(self.request,"Failed to create account")
        return super().form_invalid(form)
    

class SignInView(FormView):
    form_class=LoginForm
    template_name="login.html"

    def post(self,request,*args,**kwargs):
        form=LoginForm(request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get("username")
            pwd=form.cleaned_data.get("password")

            usr=authenticate(request,username=uname,password=pwd)
            if usr:
                login(request,usr)
                messages.success(request,'login successfull')
                return redirect("home")
            else:
                # messages.error(request,'wrong credentials')
                return render(request,self.template_name,{"form":self.form_class})

class QuizHomeView(View):
    def get(self,request,*args,**kwargs):
        qs=Category.objects.all()
        return render(request,"quiz-home.html",{"cats":qs})
    
    def post(self,request,*args,**kwargs):
        cat=request.POST.get("category")
        mode=request.POST.get("mode")
        print(cat,mode)
        return redirect("question-list",cat=cat,mode=mode)
    
from django.db.models import Sum
class QuestionListView(View):

    def get(self,request,*args,**kwargs):
        category=kwargs.get("cat")
        mode=kwargs.get("mode")
        qs=list(Questions.objects.filter(category__name=category,mode=mode))
        random.shuffle(qs)
        return render(request,"question-list.html",{"questions":qs})
    
    def post(self,request,*args,**kwargs):
        category=kwargs.get("cat")
        mode=kwargs.get("mode")
        data=request.POST.dict()
        data.pop('csrfmiddlewaretoken')
        question_attended=len(data)
        marks_obtained=0
        wrong_answer_count=0
        for q,ans in data.items():
            question=Questions.objects.get(question=q)
            right_answer_obj=question.answer
            if(right_answer_obj.options==ans):
                marks_obtained=marks_obtained+question.marks
            else:
                wrong_answer_count+=1
            right_answer_count=question_attended-wrong_answer_count
        # print(marks_obtained,question_attended,wrong_answer_count,right_answer_count)
        result=''
        total=Questions.objects.filter(category__name=category,mode=mode).aggregate(Sum('marks')).get("marks__sum")
        if marks_obtained>=total/2:
            result="pass"
        else:
         result='failed'
        # print(total)
        data=QuizRecord.objects.create(marks_obtained=marks_obtained,wrong_answer_count=wrong_answer_count,right_answer_count=right_answer_count,user=request.user,result=result)
        return render(request,"quiz-mark.html",{"marks_obtained":marks_obtained,"question_attended":question_attended,"wrong_answer_count":wrong_answer_count,"right_answer_count":right_answer_count,"result":result})
    

class QuizLIstView(ListView):
    model=QuizRecord
    template_name="quiz-list.html"
    # template_name="home.html"
    context_object_name="records"

    def get_queryset(self):
        return QuizRecord.objects.filter(user=self.request.user)
    



class SignOutView(View):
    def get(self,request,*args,**kwargs):
        logout(request)
        messages.success(request,"logout successfull")
        return redirect('signin')