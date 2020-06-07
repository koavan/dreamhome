import json
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from .models import Owner
from django.contrib.auth import get_user_model

User = get_user_model()

class OwnerListAPIViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.com', name='test')
        self.owner = Owner.objects.create(user=self.user, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)

    def test_owner_listview(self):
        response = self.client.get(reverse('owners-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class OwnerDetailAPIViewTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@test.com', name='test')
        self.owner = Owner.objects.create(user=self.user, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)

    def test_owner_detailview(self):
        response = self.client.get(reverse('owner-detail', kwargs={"pk": self.owner.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(json.loads(response.content), {
                "id":self.owner.id,
                "user":"test@test.com",
                "company_name":"test-company",
                "address":"test-address",
                "district":"test-district",
                "state":"test-state",
                "gstin":"test-gstin",
                "contact_number":"9876543210",
                "support_email_id":"test@test.com",
                "website":"https://test.com",
                "pan_number":"ABCD1234EF",
                "avatar":None
            }
        )

class OwnerCreateAPIViewTest(APITestCase):

    def setUp(self):
        self.url = reverse('create-owner')
        self.user = User.objects.create(email='test@test.com', name='test')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_ownercreateview_authenticated(self):
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
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_ownercreateview_un_authenticated(self):
        self.client.force_authenticate(user=None)
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
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(json.loads(response.content), {
                'detail': 'Authentication credentials were not provided.'
                }
            )

class BuyerCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.url = reverse('create-buyer')
        self.user = User.objects.create(email='test-buyer@test.com', name='test-buyer')
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_buyercreateview_authenticated(self):
        data = {
            "address": "test-address2",
            "district": "test-district2",
            "state": "test-state2",
            "gstin": "test-gstin2",
            "contact_number": "9597200186",
            "avatar": ""
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_buyercreateview_un_authenticated(self):
        self.client.force_authenticate(user=None)
        data = {
            "address": "test-address2",
            "district": "test-district2",
            "state": "test-state2",
            "gstin": "test-gstin2",
            "contact_number": "9597200186",
            "avatar": ""
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(json.loads(response.content), {
                'detail': 'Authentication credentials were not provided.'
                }
            )