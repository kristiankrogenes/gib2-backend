from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Developer
from .serializers import DeveloperSerializer


def api_home_view(request):
    return HttpResponse("Api for gib2 prosjekt")

class DeveloperView(APIView):
    def get(self, request):
        developers = Developer.objects.all()
        serializer = DeveloperSerializer(developers, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = DeveloperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
