from django.urls import path,include
from rest_framework import routers
from personal import views

router = routers.DefaultRouter()
router.register(r'personal', views.PersonalViewSet)

urlpatterns = [
    path('', include(router.urls))
]