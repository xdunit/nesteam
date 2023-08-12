from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import *


class GameCreateAPITestCase(APITestCase):
    def test_create_game_should_success(self):
        Genre(
            name='test genre 1',
            description='test descr 1'
        ).save()

        Studio(
            name='test studio 1',
            workers_count=123,
            games_count=45
        ).save()

        data = {
            'name': 'test game 1',
            'year': 2019,
            'genre': 1,
            'studio': 1
        }
        response = self.client.post('/games/list-create/', data)
        self.assertEqual(response.status_code, 201)

        game = Game.objects.last()
        self.assertEqual(game.name, data['name'])
        self.assertEqual(game.year, data['year'])
        self.assertEqual(game.genre.id, data['genre'])
        self.assertEqual(game.studio.id, data['studio'])

    def test_create_game_with_wrong_data_should_fail(self):
        response = self.client.post('/games/create-game-api/', {'test1': 'lorem'})
        self.assertEqual(response.status_code, 400)

    def test_create_game_via_get_request_should_return_405(self):
        data = {
            'name': 'Wrong form',
            'year': 2019,
            'genre': 1,
            'studio': 1
        }
        response = self.client.get('/games/create-game-api/', data)
        self.assertEqual(response.status_code, 405)
        games_exists = Game.objects.filter(name='Wrong form').exists()
        self.assertFalse(games_exists)
