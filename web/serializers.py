from rest_framework import serializers

from web.models import Suppliers


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suppliers
        fields = ['id', 'name', 'email', 'country', 'city', 'street', 'house_number', 'supplier']
        read_only_fields = ['id', 'debt']
        extra_kwargs = {'debt': {'read_only': True}}  # запрещает обновление поля 'debt'

