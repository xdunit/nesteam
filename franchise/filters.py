from django_filters import rest_framework as filters
from .models import GameCollection


class GameCollectionFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    games_list__name = filters.CharFilter(field_name='games_list__name', lookup_expr='icontains')

    class Meta:
        model = GameCollection
        fields = ['name', 'games_list__name']

    ordering = filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('games_list__name', 'games_list__name'),
        )
    )
