from django.shortcuts import render

# Create your views here.
from django.views.generic import View

class AdditionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"add.html")
    def post(self,request,*args,**kwargs):
        # print(request.POST)   to print the dictionary that have input values
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)
        return render(request,"add.html",{"out":result})

class SubtractionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"sub.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)+int(n2)
        print(result)
        return render(request,"sub.html",{"out":result})

class DivisionView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"div.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)/int(n2)
        print(result)
        return render(request,"div.html",{"out":result})
    

class MultiplicationView(View):
    def get (self,request,*args,**kwargs):
        return render(request,"mul.html")
    def post(self,request,*args,**kwargs):
        
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)*int(n2)
        print(result)
        return render(request,"mul.html",{"out":result})

class ModulusView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"mod.html")
    def post(self,request,*args,**kwargs):
        n1=request.POST.get("num1")
        n2=request.POST.get("num2")
        result=int(n1)%int(n2)
        print(result)
        return render(request,"mod.html",{"out":result})
    
class FactorialView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"fact.html")
    def post(self,request,*args,**kwargs):
        fact=1
        n=int(request.POST.get("num"))
        for i in range(1,n+1):
            fact=fact*i
        return render(request,"fact.html",{"out":fact})
    
class PrimenumberView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"prime.html")
    def post(self,request,*args,**kwargs):
        # isPrime=True
        n=int(request.POST.get("num"))

        flg=any([n%i==0 for i in range(2,n)])
        isPrime="Not Prime" if flg else "Prime"

        # for i in range(2,n):
        #     if(n%i==0):
        #         isPrime=False
        #         break
        return render(request,"prime.html",{"out":isPrime})
    

class IndexView(View):
    def get(self,request,*args,**kwargs):
        return render(request,"index.html")
    
      




    



