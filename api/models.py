# from statistics import geometric_mean
from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone

class Developer(models.Model):
    name = models.CharField(max_length=30)
    geom = models.PointField(blank=True, default="POINT(0.0 0.0)")

    def __str__(self):
        return self.name

class CurrentPosition(models.Model):
    test = models.PositiveIntegerField(blank=True)
    geom = models.PointField(blank=True, default="POINT(0.0 0.0)")


class GasStation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True)
    geom = models.PointField(default="POINT(0.0 0.0)")


class Price(models.Model):
    id = models.AutoField(primary_key=True)
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    diesel = models.FloatField(blank=True)
    unleaded = models.FloatField(blank=True)
    electric = models.FloatField(blank=True)