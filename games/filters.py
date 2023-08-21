from django_filters import rest_framework as filters
from .models import Game


class GameFilter(filters.FilterSet):
    name = filters.CharFilter(field_name='name', lookup_expr='icontains')
    year = filters.NumberFilter(field_name='year', lookup_expr='exact')
    genre = filters.CharFilter(field_name='genre__name', lookup_expr='icontains')
    studio = filters.CharFilter(field_name='studio__name', lookup_expr='icontains')

    class Meta:
        model = Game
        fields = ['name', 'year', 'genre', 'studio']

    ordering = filters.OrderingFilter(
        fields=(
            ('name', 'name'),
            ('year', 'year'),
            ('genre__name', 'genre__name'),
            ('studio__name', 'studio__name')
        )
    )

