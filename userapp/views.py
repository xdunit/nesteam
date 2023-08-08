from django.shortcuts import render
from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer

# Create your views here.
