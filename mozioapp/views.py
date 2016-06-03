import sys

from mozioapp.models import Provider
from mozioapp.models import Polygon
from mozioapp.models import Point
from django.http import Http404

from mozioapp.serializers import ProviderSerializer
from mozioapp.serializers import PolygonSerializer
from mozioapp.serializers import PointSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from collections import namedtuple

from osgeo import ogr
from geojson import Polygon as GEOPolygon
from polygon import MOZIOPolygon

Pt = namedtuple('Pt', 'x, y')  # Point
Edge = namedtuple('Edge', 'a, b')  # Polygon edge from a to b
Poly = namedtuple('Poly', 'name, edges')  # Polygon


class ProviderList(APIView):
    def array_map(self, polygon):
        return polygon.lat, polygon.lon

    def retrieve_by_point_location(self, lat, lon):
        polygons = Polygon.objects.all()
        providers = []
        for polygon in polygons:
            points = map(self.array_map, Point.objects.filter(polygon=polygon.id))
            if len(points) > 0:
                if MOZIOPolygon(points).contains(lat, lon):
                    print ("true")
                    providers.append(polygon.provider.id)
        return Provider.objects.filter(id__in=tuple(providers))

    def get(self, request):
        lat = request.GET.get('lat', 0)
        lon = request.GET.get('lon', 0)

        if lat is 0 and lon is 0:
            return Response(ProviderSerializer(Provider.objects.all(), many=True).data)

        return Response(ProviderSerializer(self.retrieve_by_point_location(lat, lon), many=True).data)

    def post(self, request):
        serializer = ProviderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProviderDetail(APIView):
    def get_object(self, pk):
        try:
            return Provider.objects.get(pk=pk)
        except Provider.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        return Response(ProviderSerializer(self.get_object(pk)).data)

    def put(self, request, pk):
        serializer = ProviderSerializer(self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        self.get_object(pk).delete()
        return Response(status=status.HTTP_200_OK)


class PolygonList(APIView):
    def get_object(self, pk):
        try:
            return Polygon.objects.filter(provider=Provider.objects.get(pk=pk).id)
        except Polygon.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        return Response(PolygonSerializer(self.get_object(pk), many=True).data)


class PolygonDetail(APIView):
    def post(self, request):
        serializer = PolygonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PointList(APIView):
    def get_object(self, pk):
        try:
            return Point.objects.filter(polygon=Polygon.objects.get(pk=pk).id)
        except Polygon.DoesNotExist:
            raise Http404

    def array_map(self, polygon):
        return polygon.lat, polygon.lon

    def get(self, request, pk):
        if request.GET.get('geojson', False):
            return Response(GEOPolygon(map(self.array_map, self.get_object(pk))))

        return Response(PointSerializer(self.get_object(pk), many=True).data)


class PointDetail(APIView):
    def post(self, request, pk=None):
        if pk is not None:
            serializer = PointSerializer(data=[Point(pk, point[0], point[1]) for point in ogr.CreateGeometryFromJson(request.data)], many=True)
        else:
            serializer = PointSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
