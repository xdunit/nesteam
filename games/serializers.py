from rest_framework import serializers
from .models import *


class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class StudioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'


class GenreSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


