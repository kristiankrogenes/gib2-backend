from django.db import models
from django.contrib.gis.db import models

class Developer(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class CurrentPosition(models.Model):
    test = models.PositiveIntegerField(blank=True)
    geom = models.GeometryField(blank=True)
        