from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient

from mozioapp.models import Provider
from mozioapp.models import Polygon
from mozioapp.models import Point

from mozioapp.serializers import ProviderSerializer
from mozioapp.serializers import PolygonSerializer
from mozioapp.serializers import PointSerializer


class ProviderTests(APITestCase):
    provider = {"name": "Santiago Nicolas Roca", "email": "snroca@hotmail.com",
                "phone_number": "0352515482703", "language": "ES", "currency": "0"}
    polygon = {"provider": 1, "name": 'Area A'}
    points = [{
        "polygon": 1,
        "lat": -64.19187068939209,
        "lon": -31.447922856797316
    }, {
        "polygon": 1,
        "lat": -64.20015335083008,
        "lon": -31.46102893275898
    }, {
        "polygon": 1,
        "lat": -64.18212890625,
        "lon": -31.46615371502427
    }, {
        "polygon": 1,
        "lat": -64.17397499084473,
        "lon": -31.458246790639244
    }, {
        "polygon": 1,
        "lat": -64.17539119720459,
        "lon": -31.449606980407417
    }, {
        "polygon": 1,
        "lat": -64.19187068939209,
        "lon": -31.447922856797316
    }];

    def test_post_and_get_list_provider(self):
        """
        Ensure we can create a new provider.
        """
        response = self.client.post('/provider', self.provider, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Provider.objects.count(), 1)
        self.assertEqual(Provider.objects.get().name, 'Santiago Nicolas Roca')
        self.assertEqual(Provider.objects.get().email, 'snroca@hotmail.com')
        self.assertEqual(Provider.objects.get().phone_number, '0352515482703')
        self.assertEqual(Provider.objects.get().language, 'ES')
        self.assertEqual(Provider.objects.get().currency, '0')

    def test_get_provider(self):
        """
        Ensure we can retrieve a provider.
        """
        provider = ProviderSerializer(data={"name": "Santiago Nicolas Roca", "email": "snroca@hotmail.com",
                                            "phone_number": "0352515482703", "language": "ES", "currency": "0"})
        provider.is_valid()
        provider.save()

        response = self.client.get('/provider/1')
        self.assertEqual(response.data, {"id": 1, "name": "Santiago Nicolas Roca", "email": "snroca@hotmail.com",
                                         "phone_number": "0352515482703", "language": "ES", "currency": "0"})

    def test_delete_provider(self):
        """
        Ensure we can retrieve a provider.
        """
        provider = ProviderSerializer(data=self.provider)
        provider.is_valid()
        provider.save()

        response = self.client.delete('/provider/1')
        self.assertEqual(Provider.objects.count(), 0)

    def test_put_provider(self):
        """
        Ensure we can retrieve a provider.
        """
        provider = ProviderSerializer(data=self.provider)
        provider.is_valid()
        provider.save()
        response = self.client.put('/provider/1', {"name": "Roca Santiago Nicolas", "email": "hotmail@snroca.com",
                                                   "phone_number": "3072845323", "language": "EN", "currency": "1"},
                                   format='json')

        self.assertEqual(Provider.objects.get().name, 'Roca Santiago Nicolas')
        self.assertEqual(Provider.objects.get().email, 'hotmail@snroca.com')
        self.assertEqual(Provider.objects.get().phone_number, '3072845323')
        self.assertEqual(Provider.objects.get().language, 'EN')
        self.assertEqual(Provider.objects.get().currency, '1')

    def test_post_and_get_list_polygon(self):
        """
        Ensure we can create a new provider.
        """
        provider = ProviderSerializer(data=self.provider)
        provider.is_valid()
        provider.save()
        response = self.client.post('/polygon', {"provider": 1, "name": 'Area A'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Polygon.objects.count(), 1)
        self.assertEqual(Polygon.objects.get().provider.id, 1)
        self.assertEqual(Polygon.objects.get().name, 'Area A')

    def test_get_polygon_list(self):
        """
        Ensure we can create a new provider.
        """
        provider = ProviderSerializer(data=self.provider)
        provider.is_valid()
        provider.save()

        polygon = PolygonSerializer(data=self.polygon)
        polygon.is_valid()
        polygon.save()

        response = self.client.get('/provider/1/polygon')
        response = PolygonSerializer(data=response.data, many=True)
        response.is_valid()
        self.assertEqual(response.data, [self.polygon])

    def test_post_point(self):
        """
        Ensure we can create a new provider.
        """
        provider = ProviderSerializer(data=self.provider)
        provider.is_valid()
        provider.save()

        polygon = PolygonSerializer(data=self.polygon)
        polygon.is_valid()
        polygon.save()

        response = self.client.post('/point', self.points, format='json')
        self.assertEqual(Point.objects.count(), 6)

    def test_get_point_list(self):
        """
        Ensure we can create a new provider.
        """
        provider = ProviderSerializer(data=self.provider)
        provider.is_valid()
        provider.save()

        polygon = PolygonSerializer(data=self.polygon)
        polygon.is_valid()
        polygon.save()

        point = PointSerializer(data=self.points, many=True)
        point.is_valid()
        point.save()

        response = self.client.get('/polygon/1/point')
        response = PointSerializer(data=response.data, many=True)
        response.is_valid()
        self.assertEqual(response.data, self.points)

    def test_get_providers_by_coordinate(self):
        """
        Ensure we can create a new provider.
        """
        provider = ProviderSerializer(data=self.provider)
        provider.is_valid()
        provider.save()

        polygon = PolygonSerializer(data=self.polygon)
        polygon.is_valid()
        polygon.save()

        point = PointSerializer(data=self.points, many=True)
        point.is_valid()
        point.save()

        response = self.client.get('/provider?lat=-64.18603420257568&lon=-31.45535473950899')
        response = ProviderSerializer(data=response.data, many=True)
        response.is_valid()
        self.assertEqual(len(response.data), 1)

        response = self.client.get('/provider?lat=-0.0&lon=-0.0')
        response = ProviderSerializer(data=response.data, many=True)
        response.is_valid()
        print (response.data)
        self.assertEqual(len(response.data), 0)
