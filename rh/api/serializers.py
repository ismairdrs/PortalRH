from django.contrib.auth.models import User
from website.models import Vagas, Curriculo
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class VagasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vagas
        fields = ['titulo', 'descricao', 'localizacao', 'salario', 'nome_empresa', 'email_contato']


