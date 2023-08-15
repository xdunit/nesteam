import factory
from .models import *


class GameFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Game

    name = factory.Sequence(
        lambda n: f'Test game {n}'
    )
    year = factory.Sequence(
        lambda n: n
    )
    genre = factory.SubFactory('games.factories.GenreFactory')
    studio = factory.SubFactory('games.factories.StudioFactory')


class GenreFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Sequence(
        lambda n: f'test genre name {n}'
    )
    description = factory.Sequence(
        lambda n: f'test game desc {n}'
    )


class StudioFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Studio

    name = factory.Sequence(
        lambda n: f'test studio name {n}'
    )
    workers_count = factory.Sequence(
        lambda n: n
    )
    games_count = factory.Sequence(
        lambda n: n
    )

