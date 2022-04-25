from django.core.management.base import BaseCommand
from api.models import *
import geojson
import os, sys
from django.contrib.gis.geos import Point
import requests
import random 

class Command(BaseCommand):

    def handle(self, *args, **kwargs):
        stations = GasStation.objects.all()

        for station in stations:
            try:
                price, created = Price.objects.get_or_create(
                    gas_station=station,
                    diesel = random.uniform(16, 23),
                    octane_95 = random.uniform(16, 23),
                    electric = random.uniform(16, 23)
                )
                print(f"Price {price.id} is added")
            except Exception as e:
                print("Price not valid", e)