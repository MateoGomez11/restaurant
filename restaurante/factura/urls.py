from django.urls import path,include
from rest_framework import routers
from factura import views

router = routers.DefaultRouter()
router.register(r'factura', views.FacturaViewSet)

urlpatterns = [
    path('', include(router.urls))
]