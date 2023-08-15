from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.viewsets import ModelViewSet

# Create your views here.


class FranchiseView(ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer


