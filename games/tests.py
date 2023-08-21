from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from .models import *
from .factories import *
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model



class GameCreateAPITestCase(APITestCase):
    def test_create_game_should_success(self):
        genre = Genre.objects.create(name='test genre 1', description='test descr 1')
        studio = Studio.objects.create(name='test studio 1', workers_count=123, games_count=45)

        # Genre(
        #     name='test genre 1',
        #     description='test descr 1'
        # ).save()
        #
        # Studio(
        #     name='test studio 1',
        #     workers_count=123,
        #     games_count=45
        # ).save()

        data = {
            'name': 'test game 1',
            'year': 2019,
            'genre': genre.id,
            'studio': studio.id
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


class GameCollectionTest(APITestCase):
    def setUp(self):
        self.gcol_1 = GameFactory()
        self.gcol_2 = GameFactory()
        self.gcol_3 = GameFactory()

    def test_get_list_of_3_game_collections(self):
        response = self.client.get('/games/game-test/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.gcol_1.name, response.data[0]['name'])
        self.assertEqual(self.gcol_2.name, response.data[1]['name'])
        self.assertEqual(self.gcol_3.name, response.data[2]['name'])

    def test_get_one_game_collection(self):
        response = self.client.get(f'/games/game-test/{self.gcol_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.gcol_1.name, response.data['name'])


class GenreCollectionTest(APITestCase):
    def setUp(self):
        self.genrecol_1 = GenreFactory()
        self.genrecol_2 = GenreFactory()
        self.genrecol_3 = GenreFactory()

    def test_get_list_of_3_game_collections(self):
        response = self.client.get('/games/genre/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.genrecol_1.name, response.data[0]['name'])
        self.assertEqual(self.genrecol_2.name, response.data[1]['name'])
        self.assertEqual(self.genrecol_3.name, response.data[2]['name'])

    def test_get_one_game_collection(self):
        response = self.client.get(f'/games/genre/{self.genrecol_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.genrecol_1.name, response.data['name'])


class StudioCollectionTest(APITestCase):
    def setUp(self):
        self.studiocol_1 = StudioFactory()
        self.studiocol_2 = StudioFactory()
        self.studiocol_3 = StudioFactory()

    def test_get_list_of_3_game_collections(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        token, created = Token.objects.get_or_create(user=user)

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        response = self.client.get('/games/api-studio/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.studiocol_1.name, response.data[0]['name'])
        self.assertEqual(self.studiocol_2.name, response.data[1]['name'])
        self.assertEqual(self.studiocol_3.name, response.data[2]['name'])

    # def test_get_one_game_collection(self):
    #     self.client.force_authenticate(user=None)
    #     response = self.client.get(f'/games/api-studio/{self.studiocol_1.pk}/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(self.studiocol_1.name, response.data['name'])

    def test_get_one_game_collection(self):
        user = get_user_model().objects.create_user(username='testuser', password='testpassword')
        token, created = Token.objects.get_or_create(user=user)

        self.client.credentials(HTTP_AUTHORIZATION=f'Token {token.key}')

        response = self.client.get(f'/games/api-studio/{self.studiocol_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.studiocol_1.name, response.data['name'])
