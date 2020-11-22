from django.contrib.auth.models import User
from website.models import Position, Resumo
from rest_framework import  viewsets
from .serializers import  PositionsSerializer, UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PositionsViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionsSerializer



