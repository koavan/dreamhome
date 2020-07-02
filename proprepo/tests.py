from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
import json
from profiles.models import Owner
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()

class SiteCreateAPIViewTest(APITestCase):
    url = reverse('add-site')
    data = {
        "name" : "test-site",
        "description" : "test description",
        "located_at" : "test locality",
        "latitude" : 11.1111,
        "longitude" : 12.1212,
        "area_sqft" : 100000,
        "area_cents" : 229,
        "total_properties" : 100,
        "properties_occupied" : 50,
        "properties_available" : 50,
        "land_rate_sqft" : 1300,
        "land_rate_cent" : 566800,
        "status" : 'AVAILABLE',
        "approved" : True,
        "approval_body" : "DTCP"
    }

    def setUp(self):
        self.user = User.objects.create(email='test@test.com', name='test')
        self.owner = Owner.objects.create(user=self.user, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)
        self.token = Token.objects.create(user=self.user)
        self.api_authentication()
    
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_site_creation_authenticated(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_site_creation_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(json.loads(response.content), {
                'detail': 'Authentication credentials were not provided.'
                }
            )
