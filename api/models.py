from django.db import models
from django.contrib.gis.db import models
from django.utils import timezone


class GasStation(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    brand = models.CharField(max_length=30, null=True, blank=True)
    geom = models.PointField(default="POINT(0.0 0.0)")
    county = models.CharField(max_length=30, null=True, blank=True)
    municipality = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Price(models.Model):
    id = models.AutoField(primary_key=True)
    gas_station = models.ForeignKey(GasStation, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    diesel = models.FloatField(blank=True)
    octane_95 = models.FloatField(blank=True)
    electric = models.FloatField(blank=True)

    def __str__(self):
        return "Price " + self.id + " - " + self.gas_station