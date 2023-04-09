from rest_framework import serializers




from django.contrib.auth.models import User




from quiz.models import Category,Questions,Answers




class UserSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=User
        fields=["id","username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class Categoryserializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    is_active=serializers.BooleanField(read_only=True)
    class Meta:
        model=Category
        fields="__all__"



class AnswerSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    question=serializers.CharField(read_only=True)
    class Meta:
        model=Answers
        fields=["id","question","options","is_correct"]





class QuestionSerialaizer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    category=serializers.CharField(read_only=True)
    choices=AnswerSerializer(many=True)
    class Meta:
        model=Questions
        fields=["id","category","mode","question","choices","marks"]


