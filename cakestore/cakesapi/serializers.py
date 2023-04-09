from rest_framework import serializers



from cakesapi.models import Cakes





class CakeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cakes
        fields="__all__"