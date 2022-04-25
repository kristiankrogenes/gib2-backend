from django.core.management.base import BaseCommand
from api.models import GasStation
import requests

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        stations = GasStation.objects.all()
        for i, station in enumerate(stations):
            lon, lat = station.geom.x, station.geom.y
            api_query = 'https://ws.geonorge.no/kommuneinfo/v1/punkt?nord={}&koordsys=4326&ost={}'.format(lat, lon)
            response = requests.get(api_query)
            if response.status_code==200:
                print(i)
                json_data = response.json()
                station.county = json_data['fylkesnavn']
                station.municipality = json_data['kommunenavn']
                station.save()