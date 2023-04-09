from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View
from members.models import Member

# Create your views here.


def members(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all-members.html')
  context = {
    'mymembers': mymembers,
  }
  return HttpResponse(template.render(context, request))


# class MemberView(View):
#   def get(self,request,*args,**kwargs):
#     mymembers=Member.objects.all()
#     return render(request,'all-members.html',{'mymembers':mymembers})

def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))
