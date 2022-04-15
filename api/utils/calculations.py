from api.models import GasStation, Price
from django.contrib.gis.geos import GEOSGeometry

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

    stations = GasStation.objects.all()
    for station in stations:
        if station.municipality in insights['municipality']:
            insights['municipality'][station.municipality]['total'] += 1
        else:   
            insights['municipality'][station.municipality] = {
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
        if station.county in insights['county']:
            insights['county'][station.county]['total'] += 1
        else:
            insights['county'][station.county] = {
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
    
    prices = Price.objects.all()
    for price in prices:
        diesel, octane_95, electric =  price.diesel, price.octane_95, price.electric
        insight_municipality = insights['municipality'][price.gas_station.municipality]
        insight_county = insights['county'][price.gas_station.county]

        # MUNICIPALITY 
        if diesel > insight_municipality['prices']['diesel']['max']:
            insight_municipality['prices']['diesel']['max'] = diesel
        if octane_95 > insight_municipality['prices']['octane_95']['max']:
            insight_municipality['prices']['octane_95']['max'] = octane_95
        if electric > insight_municipality['prices']['electric']['max']:
            insight_municipality['prices']['electric']['max'] = electric
        
        if diesel < insight_municipality['prices']['diesel']['min']:
            insight_municipality['prices']['diesel']['min'] = diesel
        if octane_95 < insight_municipality['prices']['octane_95']['min']:
            insight_municipality['prices']['octane_95']['min'] = octane_95
        if electric < insight_municipality['prices']['electric']['min']:
            insight_municipality['prices']['electric']['min'] = electric

        insight_municipality['prices']['diesel']['sum'] += diesel
        insight_municipality['prices']['octane_95']['sum'] += octane_95
        insight_municipality['prices']['electric']['sum'] += electric

        insight_municipality['prices']['diesel']['average'] = insight_municipality['prices']['diesel']['sum'] / insight_municipality['total']
        insight_municipality['prices']['octane_95']['average'] = insight_municipality['prices']['octane_95']['sum'] / insight_municipality['total']
        insight_municipality['prices']['electric']['average'] = insight_municipality['prices']['electric']['sum'] / insight_municipality['total']     
        
        # COUNTY 
        if diesel > insight_county['prices']['diesel']['max']:
            insight_county['prices']['diesel']['max'] = diesel
        if octane_95 > insight_county['prices']['octane_95']['max']:
            insight_county['prices']['octane_95']['max'] = octane_95
        if electric > insight_county['prices']['electric']['max']:
            insight_county['prices']['electric']['max'] = electric

        if diesel < insight_county['prices']['diesel']['min']:
            insight_county['prices']['diesel']['min'] = diesel
        if octane_95 < insight_county['prices']['octane_95']['min']:
            insight_county['prices']['octane_95']['min'] = octane_95
        if electric < insight_county['prices']['electric']['min']:
            insight_county['prices']['electric']['min'] = electric

        insight_county['prices']['diesel']['sum'] += diesel
        insight_county['prices']['octane_95']['sum'] += octane_95
        insight_county['prices']['electric']['sum'] += electric

        insight_county['prices']['diesel']['average'] = insight_county['prices']['diesel']['sum'] / insight_county['total']
        insight_county['prices']['octane_95']['average'] = insight_county['prices']['octane_95']['sum'] / insight_county['total']
        insight_county['prices']['electric']['average'] = insight_county['prices']['electric']['sum'] / insight_county['total']

    return insights