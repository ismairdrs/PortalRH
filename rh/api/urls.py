from django.urls import path, include
from django.contrib.auth.models import User
from website.models import Position
from rest_framework import routers, serializers, viewsets
from .views import  PositionsViewSet, UserViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'positions', PositionsViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]
