from django.urls import path, include
from django.contrib.auth.models import User
from website.models import Vagas
from rest_framework import routers, serializers, viewsets
from .views import  VagasViewSet, UserViewSet



router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'vagas', VagasViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    
]
