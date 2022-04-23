from rest_framework import serializers
from rest_framework_gis import serializers
from .models import County, GasStation, Price

class GasStationSerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = GasStation
        geo_field = 'geom'
        fields = '__all__'

class PriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Price
        fields = '__all__'

class CountySerializer(serializers.GeoFeatureModelSerializer):
    class Meta:
        model = County
        geo_field = 'geom'
        fields = '__all__'