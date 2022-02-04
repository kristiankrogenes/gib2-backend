from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Developer
from .serializers import DeveloperSerializer

def api_home_view(request):
    return HttpResponse("Api for gib2 prosjekt")

class DeveloperView(APIView):
    def get(self, request):
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True)
        return Response(serializer.data)
