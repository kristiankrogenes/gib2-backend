from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

def api_home_view(request):
    return HttpResponse("Api for gib2 prosjekt")
