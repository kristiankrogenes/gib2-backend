from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework_gis import serializers
from .models import Developer, GasStation

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class GasStationSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = GasStation
        geo_field = 'geom'
        fields = '__all__'