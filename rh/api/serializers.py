from django.contrib.auth.models import User
from website.models import Position, Resumo
from rest_framework import routers, serializers, viewsets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


class PositionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = ['title', 'description', 'location', 'salary', 'name_company', 'email_contact']


