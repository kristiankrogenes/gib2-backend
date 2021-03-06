from django.urls import path
from .views import FuzzyScoreView, GasStationView, api_home_view, PriceView, NearestStations, InsightView, StationsInsideRadius, CountyView, OptimizedRouteAirDistanceView

urlpatterns = [
    path('', api_home_view),
    path('gasstations/', GasStationView.as_view(), name='gasstations'),
    path('prices/', PriceView.as_view(), name='prices'),
    path('stations-inside-radius/', StationsInsideRadius.as_view(), name='stations-inside-radius'),
    path('nearest-stations/', NearestStations.as_view(), name='nearest-stations'),
    path('counties/', CountyView.as_view(), name='counties'),  
    path('insights/', InsightView.as_view(), name='data-insights'),
    path('fuzzy/', FuzzyScoreView.as_view(), name='fuzzy-score'),
    path('or-distance/', OptimizedRouteAirDistanceView.as_view(), name='fuzzy-score'),
]