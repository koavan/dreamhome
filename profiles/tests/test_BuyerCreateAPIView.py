import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from profiles.models.buyer import Buyer
from django.contrib.auth import get_user_model

User = get_user_model()

class BuyerCreateAPIViewTest(APITestCase):
    
    data = {
            "address": "test-address2",
            "district": "test-district2",
            "state": "test-state2",
            "contact_number": "9597200186",
            "avatar": ""
        }

    def setUp(self):
        self.url = reverse('create-buyer')
        self.user = User.objects.create(email='test-buyer@test.com', name='test-buyer')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_buyercreateview_authenticated(self):
        # print(self.url)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_buyercreateview_authenticated_duplicate(self):

        buyer = Buyer.objects.create(
            user = self.user,
            address = "test-address2",
            district = "test-district2",
            state = "test-state2",
            contact_number = "9597200186",
            avatar = ""
        )

        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(json.loads(response.content), {
                "detail": "You do not have permission to perform this action."
            }
        )

    def test_buyercreateview_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(json.loads(response.content), {
                'detail': 'Authentication credentials were not provided.'
                }
            )