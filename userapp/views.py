from rest_framework import generics
from rest_framework.viewsets import ModelViewSet

from . import serializers
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserSerializer

# Create your views here.
