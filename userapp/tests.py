from django.test import TestCase
from rest_framework.test import APITestCase
from django.contrib.auth import get_user_model


class AuthenticationTest(APITestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(username='testuser', password='testpassword')

    def test_jwt_authentication(self):
        url = '/auth/jwt/create/'
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }

        response = self.client.post(url, data)

        self.assertEqual(response.status_code, 200)
        self.assertIn('access', response.data)


# Create your tests here.
