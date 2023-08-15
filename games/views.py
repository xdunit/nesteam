from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from .models import *
from rest_framework import generics


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


class StudioViewSet(ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioSerializers


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
