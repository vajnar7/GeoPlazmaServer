from django.db import models
from django.utils.translation import ugettext_lazy as _


class Area(models.Model):
    name = models.CharField(max_length=32, verbose_name=_('Ime'))

    def __str__(self):
        return "Area: %s" % self.name


class GeoPoint(models.Model):
    area = models.OneToOneField(Area, verbose_name=_('Območje'), on_delete=models.CASCADE, primary_key=True)
    lon = models.FloatField(verbose_name=_('GEO dolžina'))
    lat = models.FloatField(verbose_name=_('GEO širina'))

    def __str__(self):
        return "GeoPoint: %s" % self.area
