from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Q
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .filters import GameFilter
from games.serializers import GameSerializers, GenreSerializers, StudioSerializers
from .models import *
from games.paginations import GenrePagination
from rest_framework import generics, status
from rest_framework.generics import ListAPIView, CreateAPIView


# Create your views here.


# def games_list(request):
#     game_lst = Game.objects.all()
#     serializer = GameSerializers(game_lst, many=True)
#     data = serializer.data
#     return JsonResponse(data, safe=False)


# def studios(request):
#     studio_lst = Studio.objects.all()
#     serializer = StudioSerializers(studio_lst, many=True)
#     data = serializer.data
#     return JsonResponse(data, safe=False)


# class GameCreateAPI(generics.CreateAPIView):
#     queryset = Game.objects.all()
#     serializer_class = serializers.GameSerializers

class GameViewTest(ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializers


class GamesView(generics.ListCreateAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializers
    pagination_class = GenrePagination


class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all().order_by('id')
    serializer_class = StudioSerializers
    permission_classes = [IsAuthenticated]


class GameCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = GameSerializers(data=data)
        if serializer.is_valid():
            game = Game()
            game.name = serializer.validated_data['name']
            game.year = serializer.validated_data['year']
            game.genre = serializer.validated_data['genre']
            game.studio = serializer.validated_data['studio']
            game.save()

            serializer = GameSerializers(instance=game)
            return Response(
                data=serializer.data,
                status=201
            )
        else:
            errors = serializer.error_messages
            response_data = {
                'message': 'dannie ne validni',
                'errors': errors
            }
            return Response(
                data=response_data,
                status=400
            )


class GameListView(ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializers
    filterset_class = GameFilter
    search_fields = ['name', 'year', 'genre', 'studio']


class GamesSearchView(APIView):
    def get(self, request):
        if 'key_word' in request.GET:
            key_word = request.GET['key_word']
        elif 'key_word' in request.data:
            key_word = request.data['key_word']
        else:
            return Response('no data', status=400)

        games = Game.objects.filter(
            Q(name__icontains=key_word) |
            Q(genre__name__icontains=key_word) |
            Q(studio__name__icontains=key_word)
        )

        serializer = GameSerializers(instance=games, many=True)
        json_data = serializer.data
        return Response(data=json_data)


