from rest_framework.test import APITestCase

from userapp.factories import UserFactory
from .factories import CollectionFactory
from .models import GameCollection


# from django.urls import reverse

# Create your tests here.


class CollectionTest(APITestCase):
    def setUp(self):
        self.col_1 = CollectionFactory()
        self.col_2 = CollectionFactory()
        self.col_3 = CollectionFactory()

    def test_get_list_of_3_collections(self):
        response = self.client.get('/franchise/collection/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data[0]['name'])
        self.assertEqual(self.col_2.name, response.data[1]['name'])
        self.assertEqual(self.col_3.name, response.data[2]['name'])

    def test_get_one_collection(self):
        response = self.client.get(f'/franchise/collection/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.col_1.name, response.data['name'])

    def test_create_collection(self):
        data = {
            'name': 'New Collection'
        }
        response = self.client.post('/franchise/collection/', data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(GameCollection.objects.count(), 4)

    def test_update_collection(self):
        data = {
            'name': 'Updated Collection'
        }
        response = self.client.put(f'/franchise/collection/{self.col_1.pk}/', data)
        self.assertEqual(response.status_code, 200)
        updated_collection = GameCollection.objects.get(pk=self.col_1.pk)
        self.assertEqual(updated_collection.name, data['name'])

    def test_delete_collection(self):
        response = self.client.delete(f'/franchise/collection/{self.col_1.pk}/')
        self.assertEqual(response.status_code, 204)
        self.assertFalse(GameCollection.objects.filter(pk=self.col_1.pk).exists())

