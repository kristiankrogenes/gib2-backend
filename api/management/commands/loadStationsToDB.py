from django.core.management.base import BaseCommand
from api.models import *
import geojson
import os, sys
from django.contrib.gis.geos import Point

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        filepath = os.path.join(sys.path[0], "stations.geojson")
        with open(filepath, encoding='utf8') as f:
            gj = geojson.load(f)
        for station in gj['features']:
            try:
                GS, created = GasStation.objects.get_or_create(
                    name=station['properties']['name'],
                    brand=station['properties']['brand'],
                    geom=Point(float(station['geometry']['coordinates'][0]), float(station['geometry']['coordinates'][1]), srid=4326)
                )
            except:
                print("Gas station not allowed")