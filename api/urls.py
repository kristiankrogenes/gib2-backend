from django.urls import path
from .views import api_home_view

urlpatterns = [
    path('', api_home_view),
]