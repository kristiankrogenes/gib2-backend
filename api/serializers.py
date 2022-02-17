from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import Developer, GasStation

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class GasStationSerializer(serializers.ModelSerializer):
    class Meta:
        model = GasStation
        fields = '__all__'