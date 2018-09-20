from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from areas.models import Area, GeoPoint


class UpdateGeoPoint(APIView):
    permission_classes = (IsAuthenticated,)

    def _get_area(self, name):
        try:
            return Area.objects.get(name=name)
        except ObjectDoesNotExist:
            return Area.objects.create(name=name)

    def get(self, request, format=None, area_name=None):
        area = self._get_area(area_name)
        h = GeoPoint.objects.filter(area=area)
        res = {g.id: g.lon for g in GeoPoint.objects.filter(area=area)}
        return Response(res)

    def put(self, request, format=None, area_name=None):
        lon = request.data.get("lon", 0)
        lat = request.data.get("lat", 0)
        area = self._get_area(area_name)
        print(lon)
        print(lat)
        print(area)

        GeoPoint.objects.create(area=area, lon=lon, lat=lat)
        return Response(dict(err_code="OK"))


class GeoPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoPoint
        fields = ('lon', 'lat')
