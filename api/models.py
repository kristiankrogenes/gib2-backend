from django.db import models
from django.contrib.gis.db import models

class Developer(models.Model):
    name = models.CharField(max_length=30)
    geom = models.PointField(blank=True, default="POINT(0.0 0.0)")

    def __str__(self):
        return self.name

class CurrentPosition(models.Model):
    test = models.PositiveIntegerField(blank=True)
    geom = models.PointField(blank=True, default="POINT(0.0 0.0)")
        