
from django.contrib import admin
from django.urls import path,include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title='Ecommerce-Backend',
        description='Backend for online market',
        default_version='v1',
        terms_of_service="default_terms",
        contact=openapi.Contact(email='aa2004bek@gmail.com'),
        license=openapi.License(name='default_license')
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/',include('users.urls')),
    path('api/cart/',include('cart.urls')),
    path('api/order/',include('order.urls')),
    path('api/market/',include('market.urls')),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='schema-redoc')
]
