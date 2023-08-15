from rest_framework.serializers import ModelSerializer
from .models import *


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = GameCollection
        fields = '__all__'
