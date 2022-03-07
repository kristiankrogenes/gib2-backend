from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from rest_framework_gis import serializers
from .models import Developer, GasStation, Price

class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'

class GasStationSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = GasStation
        geo_field = 'geom'
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'