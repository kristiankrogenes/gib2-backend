from api.models import GasStation
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