from .serializers import *
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .filters import GameCollectionFilter

# Create your views here.


class FranchiseView(ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer


class GameCollectionAPIView(ListAPIView):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer
    filterset_class = GameCollectionFilter
    search_fields = ['name', 'games_list__name']

