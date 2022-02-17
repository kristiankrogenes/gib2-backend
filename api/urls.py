from django.urls import path
from .views import GasStationView, api_home_view, DeveloperView

urlpatterns = [
    path('', api_home_view),
    path('developers/', DeveloperView.as_view(), name='developers'),
    path('gasstations/', GasStationView.as_view(), name='gasstations'),
]