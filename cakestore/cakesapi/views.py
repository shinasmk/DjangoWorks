from django.shortcuts import render



from rest_framework import viewsets
# Create your views here.



from cakesapi.serializers import CakeSerializer
from cakesapi.models import Cakes



class CakeView(viewsets.ModelViewSet):
    serializer_class=CakeSerializer
    model=Cakes
    queryset=Cakes.objects.all()
