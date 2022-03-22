from api.models import GasStation
from django.contrib.gis.geos import GEOSGeometry

def find_nearest_stations(lon, lat):
    current_position = GEOSGeometry('POINT(' + str(lon) + ' ' + str(lat) + ')', srid=4326)  
    all_stations = GasStation.objects.all()
    print(all_stations)
    nearest_stations  = [None, None, None]
    for station in all_stations:
        dist = current_position.distance(station.geom)
        print(station, dist)
        for i, s in enumerate(nearest_stations):
            if s == None:
                nearest_stations[i] = station
                break
            elif dist < current_position.distance(s.geom) and None not in nearest_stations:
                nearest_stations[i] = station
                break
    return nearest_stations
