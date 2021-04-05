import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from profiles.models.owner import Owner
from django.contrib.auth import get_user_model

User = get_user_model()

class OwnerCreateAPIViewTest(APITestCase):

    data = {
            "company_name": "test-company2",
            "address": "test-address2",
            "district": "test-district2",
            "state": "test-state2",
            "gstin": "test-gstin2",
            "contact_number": "9876540123",
            "support_email_id": "test2@test.com",
            "website": "https://test.com",
            "pan_number": "ABCD1234EF",
        }

    def setUp(self):
        self.url = reverse('create-owner')
        self.user = User.objects.create(email='test@test.com', name='test')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_ownercreateview_authenticated(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_ownercreateview_authenticated_duplicate(self):

        owner = Owner.objects.create(
            user = self.user,
            company_name = "test-company2",
            address = "test-address2",
            district = "test-district2",
            state = "test-state2",
            gstin = "test-gstin2",
            contact_number = "9876501234",
            support_email_id = "test3@test.com",
            website = "https://test.com",
            pan_number = "ABCD1234EF",
        )
        response = self.client.post(self.url, self.data)
        # print(response.content)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(json.loads(response.content), {
                "detail": "You do not have permission to perform this action."
            }
        )

    def test_ownercreateview_un_authenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(json.loads(response.content), {
                'detail': 'Authentication credentials were not provided.'
                }
            )