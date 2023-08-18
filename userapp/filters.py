from django_filters import rest_framework as filters
from .models import Player


class PlayerFilter(filters.FilterSet):

    nick = filters.CharFilter(field_name='nick', lookup_expr='icontains')

    class Meta:
        model = Player
        fields = ['nick']
