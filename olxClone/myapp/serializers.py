from rest_framework import serializers
from django.contrib.auth.models import User
from api.models import Category,Vehicles,VehiclePics,Wishlist,Questions,Answers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]
        
    def create(self, validated_data):                        # for password encription
        return User.objects.create_user(**validated_data)
    

class CategorySerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Category
        fields="__all__"



class VehiclePicsSerializers(serializers.ModelSerializer):
    class Meta:
        model=VehiclePics
        fields=["images"]




class WishlistSerializer(serializers.Serializer):
    user=serializers.CharField(read_only=True)
    vehicle=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    class Meta:
        model=Wishlist
        fields=["user","vehicle","date"]



class AnswerSerializer(serializers.ModelSerializer):
    ownwer=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    question=serializers.CharField(read_only=True)

    class Meta:
        model=Answers
        fields="__all__"

class QuestionSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    user=serializers.CharField(read_only=True)
    add=serializers.CharField(read_only=True)
    date=serializers.CharField(read_only=True)
    question_answer=AnswerSerializer(read_only=True,many = True)
    class Meta:
        model=Questions
        fields=["id","user","add","date","question_answer"]



class VehicleSerializers(serializers.ModelSerializer):
    owner=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)
    vehicle_images=VehiclePicsSerializers(many=True,read_only=True)
    querys=QuestionSerializer(read_only=True,many=True)

    class Meta:
        model=Vehicles
        fields="__all__"


