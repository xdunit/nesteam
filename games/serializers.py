from rest_framework import serializers
from .models import Game


class GameSerializers(serializers.ModelSerializer):
    class Meta:

        model = Game
        fields = '__all__'
