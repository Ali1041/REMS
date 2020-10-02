import django_filters

from .models import *


class SellerPropertyFilter(django_filters.FilterSet):
    class Meta:
        model = SellerProperty
        fields = ('size', 'by','purpose')
