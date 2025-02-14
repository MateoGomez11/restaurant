from django.urls import path,include
from rest_framework import routers
from producto import views

router = routers.DefaultRouter()
router.register(r'productos', views.ProductoViewSet)

urlpatterns = [
    path('', include(router.urls))
]