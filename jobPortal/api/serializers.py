from rest_framework import serializers

from api.models import Jobs,Companies

class JobSerializers(serializers.ModelSerializer):
    class Meta:
        model=Jobs
        fields="__all__"


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=Companies
        fields="__all__"