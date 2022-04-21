from django.core.management.base import BaseCommand
from api.models import County
import geojson
import os, sys
from django.contrib.gis.geos import Point, Polygon

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        module_dir = os.path.dirname(__file__)
        file_path = os.path.join(module_dir, "counties.geojson")
        with open(file_path, encoding='utf8') as f:
            counties = geojson.load(f)
        for county in counties['features']:
            try:
                c, created = County.objects.get_or_create(
                    id=county['properties']['fylkesnummer'],
                    name=county['properties']['navn']['navn'],
                    geom=Polygon(county['geometry']['coordinates'])
                )
            except:
                print("County not allowed")