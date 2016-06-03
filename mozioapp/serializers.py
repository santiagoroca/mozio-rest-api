from mozioapp.models import Provider
from mozioapp.models import Polygon
from mozioapp.models import Point

from rest_framework import serializers

class ProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provider
        fields = ('id', 'name', 'email', 'phone_number', 'language', 'currency')


class PolygonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Polygon
		fields = ('id', 'provider', 'name')


class PointSerializer(serializers.ModelSerializer):
	class Meta:
		model = Point
		fields = ('id', 'polygon', 'lat', 'lon')