from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import authentication
from rest_framework import permissions

from django_filters.rest_framework import DjangoFilterBackend




from quiz.models import Category,Questions,Answers
from quiz.serializers import Categoryserializer,QuestionSerialaizer,AnswerSerializer




class CategoriesView(viewsets.ModelViewSet):
    serializer_class=Categoryserializer
    queryset=Category.objects.all()
    # authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

# localhost:8000/api/v1/catogories/{id}/add_question
    @action(methods=["post"],detail=True)
    def add_question(self,request,*args,**kwargs):
        serializer=QuestionSerialaizer(data=request.data)
        if serializer.is_valid():
            serializer.save(category=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)
        

class QuestionView(viewsets.ModelViewSet):
    serializer_class=QuestionSerialaizer
    queryset=Questions.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["marks","mode"]
    # authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    @action(methods=["post"],detail=True)
    def add_answer(self,request,*args,**kwargs):
        serializer=AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(question=self.get_object())
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)



    # def list(self, request, *args, **kwargs):
    #     qs=Questions.objects.all()
    #     if "category" in request.query_params:
    #         cat=request.query_params.get("category")
    #         qs=qs.filter(category__name__i=cat)
    #     serializer=QuestionSerialaizer(qs,many=True)
    #     return Response(data=serializer.data)

# localhost:8000/api/v2/questions/(id)/add_answer/

