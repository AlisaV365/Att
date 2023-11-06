from .models import Suppliers
from .serializers import SupplierSerializer
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from django_filters.rest_framework import DjangoFilterBackend
from web.filters import SupplierFilter
from rest_framework import permissions


class IsActiveEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        """Проверка, является ли пользователь авторизованным и активным"""
        return request.user.is_authenticated and request.user.is_active and request.user.is_employee

class SupplierAPIView(ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Suppliers.objects.all()
    permission_classes = [IsActiveEmployee]


class SupplierRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SupplierSerializer
    queryset = Suppliers.objects.all()
    lookup_field = 'id'
    permission_classes = [IsActiveEmployee]


class SupplierFilterAPIView(ListAPIView):
    serializer_class = SupplierSerializer
    queryset = Suppliers.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = SupplierFilter
    permission_classes = [IsActiveEmployee]

