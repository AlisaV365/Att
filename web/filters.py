from django_filters import rest_framework as filters
from .models import Suppliers

class SupplierFilter(filters.FilterSet):
    country = filters.CharFilter(field_name='country') # фильтр по стране

    class Meta:
        model = Suppliers
        fields = ['country']
