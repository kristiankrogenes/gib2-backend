from api.models import GasStation, Price
from django.contrib.gis.geos import GEOSGeometry
from copy import deepcopy
from api.models import GasStation
import requests

def find_nearest_stations(lon, lat):
    current_position = GEOSGeometry('POINT(' + str(lon) + ' ' + str(lat) + ')', srid=4326)  
    all_stations = GasStation.objects.all()
    nearest_stations  = [None, None, None]
    for station in all_stations:
        dist = current_position.distance(station.geom)
        for i, st in enumerate(nearest_stations):
            if st == None:
                nearest_stations[i] = station
                break
            elif dist < current_position.distance(st.geom) and not None in nearest_stations:
                nearest_stations.insert(i, station)
                nearest_stations.pop(3)
                break
    return nearest_stations

def get_stations_inside_radius(lon, lat, rad):
    current_position = GEOSGeometry('POINT(' + str(lon) + ' ' + str(lat) + ')', srid=4326)  
    stations = GasStation.objects.all()
    stations_inside_radius = []
    for station in stations:
        dist = current_position.distance(station.geom) * 100 # Distance in km
        if dist <= rad:
            stations_inside_radius.append(station)
    return stations_inside_radius

def get_data_insights():
    insights = {
        'county': {},
        'municipality': {}
    }

    insights_template = {
        'total': 1,
        'prices': {
            'diesel': {
                'max': -1,
                'min': 100,
                'average': None,
                'sum': 0
            },
            'octane_95': {
                'max': -1,
                'min': 100,
                'average': None,
                'sum': 0
            },
            'electric': {
                'max': -1,
                'min': 100,
                'average': None,
                'sum': 0
            }
        }
    }
    def update_insights(insight_dict, fuels):
        for key, value in fuels.items():
            if value > insight_dict['prices'][key]['max']:
                insight_dict['prices'][key]['max'] = value
            if value < insight_dict['prices'][key]['min']:
                insight_dict['prices'][key]['min'] = value
            insight_dict['prices'][key]['sum'] += value
            insight_dict['prices'][key]['average'] = insight_dict['prices'][key]['sum'] / insight_dict['total']

    stations = GasStation.objects.all()
    for station in stations:
        if station.municipality in insights['municipality']:
            insights['municipality'][station.municipality]['total'] += 1
        else:   
            insights['municipality'][station.municipality] = deepcopy(insights_template)
        if station.county in insights['county']:
            insights['county'][station.county]['total'] += 1
        else:
            insights['county'][station.county] = deepcopy(insights_template)
    
    prices = Price.objects.all()
    for price in prices:
        fuels =  {'diesel': price.diesel, 'octane_95': price.octane_95, 'electric': price.electric}
        insight_municipality = insights['municipality'][price.gas_station.municipality]
        insight_county = insights['county'][price.gas_station.county]

        update_insights(insight_municipality, fuels)
        update_insights(insight_county, fuels)
    default_histogram = {'0': 0, '16': 0, '17': 0, '18': 0, '19': 0, '20': 0, '21': 0, '22': 0, '23': 0}
    histogram = { 
      'diesel': deepcopy(default_histogram),
      'octane_95': deepcopy(default_histogram),
      'electric': deepcopy(default_histogram)
    }
    values = [0, 16, 17, 18, 19, 20, 21, 22, 23]    
    for price in prices:
      fuels =  {'diesel': price.diesel, 'octane_95': price.octane_95, 'electric': price.electric}
      for key, value in fuels.items():
        for i in range(1, len(values)):
          if i == len(values) - 1 and value >= values[i]:
            histogram[key][i] += 1
          if values[i-1] <= value < values[i]:
            histogram[key][str(values[i-1])] += 1
    
    insights['histogram'] = histogram

    return insights

def updateMuniCounty(data):
    station = GasStation.objects.get(name=data['name'])
    lon, lat = station.geom.x, station.geom.y
    api_query = 'https://ws.geonorge.no/kommuneinfo/v1/punkt?nord={}&koordsys=4326&ost={}'.format(lat, lon)
    response = requests.get(api_query)
    if response.status_code==200:
            json_data = response.json()
            station.county = json_data['fylkesnavn']
            station.municipality = json_data['kommunenavn']
            station.save()

