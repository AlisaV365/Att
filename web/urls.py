from django.urls import path
from web.apps import WebConfig
from rest_framework import routers
from .views import SupplierAPIView
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Snippets API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

app_name = WebConfig.name

router = routers.DefaultRouter()
router.register(r'suppliers', SupplierAPIView)

urlpatterns = [
    path('suppliers/', SupplierAPIView.as_view(), name='suppliers'),
    path('suppliers/<int:pk>/', SupplierAPIView.as_view(), name='suppliers_detail'),
    path('suppliers/<int:pk>/update/', SupplierAPIView.as_view(), name='suppliers_update'),
    path('suppliers/create/', SupplierAPIView.as_view(), name='suppliers_create'),
    path('suppliers/<int:pk>/delete/', SupplierAPIView.as_view(), name='suppliers_delete'),

    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
