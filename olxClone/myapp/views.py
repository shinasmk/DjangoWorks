from django.shortcuts import render
from django.contrib.auth.models import User
import django_filters.rest_framework



from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import authentication
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework import status


from myapp.serializers import UserSerializer,CategorySerializer,VehicleSerializers,VehiclePicsSerializers,WishlistSerializer,QuestionSerializer,AnswerSerializer
from api.models import Category,Vehicles,Wishlist,Questions



# Create your views here.

class RegistationView(viewsets.GenericViewSet,mixins.CreateModelMixin):
    serializer_class=UserSerializer
    queryset=User.objects.all()

class CategoriesView(viewsets.ModelViewSet):
    serializer_class=CategorySerializer
    model=Category
    queryset=Category.objects.all()
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=["post"],detail=True)
    def add_vehicle(self,request,*args,**kwargs):     # custom method we created for add vehicle inside category view
        cat=self.get_object()        # used for getting objects from Category model like "pk"
        serializer=VehicleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user,category=cat)
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class VehicleView(viewsets.ModelViewSet):
    serializer_class=VehicleSerializers
    queryset=Vehicles.objects.all()
    http_method_names=["post","get","put","delete"]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    # filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    # filterset_fields = ['location']

    def list(self, request, *args, **kwargs):
     qs=Vehicles.objects.all()
     if "category" in request.query_params:
            cat=request.query_params.get("category")
            qs=qs.filter(category__name=cat)
     if "location" in request.query_params:
         loc=request.query_params.get("location")
         qs=qs.filter(location=loc)
            
     serializer=VehicleSerializers(qs,many=True)
     return Response(data=serializer.data)
    
    
#localhost:8000/api/v2/vehicles/2/add_image


    @action(methods=["post"],detail=True)
    def add_image(self,request,*args,**kwargs):
        serializer=VehiclePicsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save(vehicle=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
   
   
    @action(methods=["post"],detail=True)
    def wish_list(self,request,*args,**kwargs):
        veh=self.get_object()
        usr=request.user
        Wishlist.objects.create(vehicle=veh,user=usr)
        return Response(data="item has been added",status=status.HTTP_201_CREATED)

#localhost:8000/api//v2/vehicle/2/ask_question

    @action(methods=["post"],detail=True)
    def ask_question(self,request,*args,**kwargs):
        serializer=QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user,add=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        


class WishlistView(viewsets.ModelViewSet):
    serializer_class=WishlistSerializer
    model=Wishlist
    queryset=Wishlist.objects.all()
    http_method_names=["put","get","patch","delete"]
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]



    def list(self, request, *args, **kwargs):
        qs=Wishlist.objects.filter(user=request.user)
        serializer=WishlistSerializer(qs,many=True)
        return Response(data=serializer.data)




class QuestionsView(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    model = Questions
    queryset = Questions.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=["post"],detail=True)
    def add_answer(self,request,*args,**kwargs):
        serializer=AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(ownwer=request.user,question=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        



# localhost:8000/api/v2/questions/qid/add_answer




















