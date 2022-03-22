from django.core.management.base import BaseCommand
from api.models import *
import geojson
import os, sys
from django.contrib.gis.geos import Point

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "stations.geojson")
        with open(file_path, encoding='utf8') as f:
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