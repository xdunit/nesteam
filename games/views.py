from django.shortcuts import render
from django.http import JsonResponse
from .models import Game
from .serializers import *


# Create your views here.


def games_list(request):
    game_lst = Game.objects.all()
    serializer = GameSerializers(game_lst, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)
