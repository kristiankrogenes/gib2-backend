from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import County, GasStation, Price
from .serializers import GasStationSerializer, PriceSerializer, CountySerializer
from .utils import calculations


def api_home_view(request):
    return HttpResponse("Api for gib2 prosjekt")

class GasStationView(APIView):

    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        gasstations = GasStation.objects.all()
        serializer = GasStationSerializer(gasstations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data
        serializer = GasStationSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            calculations.updateMuniCounty(data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PriceView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        prices = Price.objects.all()
        serializer = PriceSerializer(prices, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = PriceSerializer(data=request.data)
        # user = request.user
        if serializer.is_valid():
            serializer.save()
            # user.score += 1
            # user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class NearestStations(APIView):
    def get(self, request, *args, **kwargs):
        stations = calculations.find_nearest_stations(request.query_params['lon'], request.query_params['lat'])
        serializer = GasStationSerializer(stations, many=True)
        return Response(serializer.data)

class StationsInsideRadius(APIView):
    def get(self, request, *args, **kwargs):
        radius = 20
        stations = calculations.get_stations_inside_radius(
            request.query_params['lon'], 
            request.query_params['lat'],
            radius
        )
        serializer = GasStationSerializer(stations, many=True)
        return Response(serializer.data)

class InsightView(APIView):
    def get(self, request):
        insights = calculations.get_data_insights()
        return Response(insights)

class CountyView(APIView):
    def get(self, request):
        counties = County.objects.all()
        serializer = CountySerializer(counties, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CountySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class FuzzyScoreView(APIView):
     def get(self, request, *args, **kwargs):
        score = calculations.get_fuzzy_route(
            float(request.query_params['price_weight']),
            float(request.query_params['duration_weight']),
            [float(request.query_params['start_lng']), float(request.query_params['start_lat'])],
            request.query_params['fuel_type']
         )
        return Response(score)

class OptimizedRouteAirDistanceView(APIView):
     def get(self, request, *args, **kwargs):
        print("!!!!!!!")
        route = calculations.get_closest_route_to_station(
            [float(request.query_params['start_lng']), float(request.query_params['start_lat'])]
         )
        return Response(route)
