from django.urls import path
from .views import GasStationView, api_home_view, PriceView, NearestStations, InsightView, CountyView

urlpatterns = [
    path('', api_home_view),
    path('gasstations/', GasStationView.as_view(), name='gasstations'),
    path('prices/', PriceView.as_view(), name='prices'),
    path('counties/', CountyView.as_view(), name='counties'),
    path('nearest-stations', NearestStations.as_view(), name='nearest-stations'),   
    path('insights/', InsightView.as_view(), name='data-insights'),
]