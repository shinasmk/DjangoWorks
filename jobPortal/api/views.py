from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from api.models import Jobs,Companies
from rest_framework.response import Response
from api.serializers import JobSerializers,CompanySerializer
from rest_framework.viewsets import ViewSet

class JobView(APIView):

    def get(self,request,*args,**kwargs):
        qs=Jobs.objects.all()
        serializer=JobSerializers(qs,many=True)
        return Response(data=serializer.data)
    
    def post(self,request,*args,**kwargs):
        serializer=JobSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        
        else:
            return Response(data=serializer.errors)
        

class JobDetailView(APIView):
    
    def get(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Jobs.objects.get(id=id)
        serializer=JobSerializers(qs,many=False)
        return Response(data=serializer.data)
    

    def put(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Jobs.objects.get(id=id)
        serializer=JobSerializers(instance=obj,data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

    def delete(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        obj=Jobs.objects.get(id=id)
        obj.delete()
        return Response(data="deleted")
         

"""=============================================================================="""

class CompanyView(ViewSet):
    def list(self,request,*args,**kwargs):
        qs=Companies.objects.all()
        serializer=CompanySerializer(qs,many=True)
        return Response(data=serializer.data)
    
    def create(self,request,*args,**kwargs):
        serializer=CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        
    
    def update(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Companies.objects.get(id=id)
        serializer=CompanySerializer(instance=qs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        qs=Companies.objects.get(id=id)
        serializer=CompanySerializer(qs,many=False)
        return Response(data=serializer.data)

    
    def destroy(self,request,*args,**kwargs):
        id=kwargs.get('pk')
        Companies.objects.get(id=id).delete()
        return Response(data="deleted")


        


