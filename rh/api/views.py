from django.contrib.auth.models import User
from website.models import Vagas, Curriculo
from rest_framework import  viewsets
from .serializers import  VagasSerializer, UserSerializer
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class VagasViewSet(viewsets.ModelViewSet):
    queryset = Vagas.objects.all()
    serializer_class = VagasSerializer



