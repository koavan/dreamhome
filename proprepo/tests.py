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

    def setUp(self):
        self.user = User.objects.create(email='test@test.com', name='test')
        self.owner = Owner.objects.create(user=self.user, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)

    def test_site_creation_authenticated(self):
        print(self.url)
