from __future__ import unicode_literals

from django.db import models


class Provider(models.Model):
    name = models.TextField()
    email = models.TextField()
    phone_number = models.TextField()
    language = models.CharField(max_length=100)
    currency = models.TextField()


class Polygon(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.TextField()


class Point(models.Model):
    polygon = models.ForeignKey(Polygon, on_delete=models.CASCADE)
    lat = models.FloatField()
    lon = models.FloatField()
