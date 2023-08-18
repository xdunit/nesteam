from rest_framework import generics
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView

from .filters import PlayerFilter
from .models import *
from .serializers import *

from . import serializers
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer


class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filterset_class = PlayerFilter
    search_fields = ['nick']

    # def get(self, request):
    #     players = Player.objects.all()
    #     serializer = PlayerSerializer(instance=players, many=True)
    #     return Response(data=serializer.data)

# Create your views here.
