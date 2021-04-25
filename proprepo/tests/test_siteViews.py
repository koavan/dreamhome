from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
import json
from profiles.models.owner import Owner
from profiles.models.buyer import Buyer
from proprepo.models.site import Site
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
        self.user1 = User.objects.create(email='test@test.com', name='test', phone='11111111')
        self.owner = Owner.objects.create(user=self.user1, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)

        self.user2 = User.objects.create(email='test2@test.com', name='test2', phone='22222222')
        self.buyer = Buyer.objects.create(user=self.user2,
            address='test-address-2', 
            district='test-district-2', state='test-state-2',
            contact_number='9814343210',
            avatar=None)

        self.token1 = Token.objects.create(user=self.user1)
        self.api_authentication(self.token1.key)
    
    def api_authentication(self, key):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + key )

    def test_site_creation_authenticated(self):
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_site_creation_duplicate(self):
        data2 = {
            "name" : "test-site-2",
            "description" : "test description two",
            "located_at" : "test locality two",
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
        response = self.client.post(self.url, data2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_site_creation_unauthenticated(self):
        self.client.force_authenticate(user=None)
        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(json.loads(response.content), {
                'detail': 'Authentication credentials were not provided.'
                }
            )

    def test_site_creation_for_buyer(self):
        self.token2 = Token.objects.create(user=self.user2)
        self.api_authentication(self.token2.key)

        response = self.client.post(self.url, self.data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(json.loads(response.content), {
                    "detail": "You do not have permission to perform this action."
                }
            )

class SiteDetailAPIViewTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='test@test.com', name='test', phone='11111111')
        self.owner = Owner.objects.create(user=self.user1, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)
        self.site = Site.objects.create(
            name = "test-site",
            description = "test description",
            owner_id = self.owner,
            located_at = "test locality",
            latitude = 11.1111,
            longitude = 12.1212,
            area_sqft = 100000,
            area_cents = 229,
            total_properties = 100,
            properties_occupied = 50,
            properties_available = 50,
            land_rate_sqft = 1300,
            land_rate_cent = 566800,
            status = 'AVAILABLE',
            approved = True,
            approval_body = "DTCP"
        )
        self.data = {
            "id" : self.site.id,
            "name" : "test-site",
            "description" : "test description",
            "owner_id" : self.owner.id,
            "owner_name" : self.owner.company_name,
            "located_at" : "test locality",
            "latitude" : 11.1111,
            "longitude" : 12.1212,
            "area_sqft" : 100000.0,
            "area_cents" : 229.0,
            "total_properties" : 100,
            "properties_occupied" : 50,
            "properties_available" : 50,
            "land_rate_sqft" : 1300,
            "land_rate_cent" : 566800,
            "status" : 'AVAILABLE',
            "approved" : True,
            "approval_body" : "DTCP",
            "images" : []
        }
        
    def test_site_detail_view(self):
        response = self.client.get(reverse('site-detail', kwargs={ 'pk' : self.site.id }))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            self.data
        )

class SiteListAPIViewTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='test@test.com', name='test', phone='11111111')
        self.owner = Owner.objects.create(user=self.user1, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)
        self.site1 = Site.objects.create(
            name = "test-site-1",
            description = "test description one",
            owner_id = self.owner,
            located_at = "test locality one",
            latitude = 11.1111,
            longitude = 12.1212,
            area_sqft = 100000,
            area_cents = 229,
            total_properties = 100,
            properties_occupied = 50,
            properties_available = 50,
            land_rate_sqft = 1300,
            land_rate_cent = 566800,
            status = 'AVAILABLE',
            approved = True,
            approval_body = "DTCP"
        )

        self.site2 = Site.objects.create(
            name = "test-site-2",
            description = "test description two",
            owner_id = self.owner,
            located_at = "test locality two",
            latitude = 11.1111,
            longitude = 12.1212,
            area_sqft = 100000,
            area_cents = 229,
            total_properties = 100,
            properties_occupied = 50,
            properties_available = 50,
            land_rate_sqft = 1300,
            land_rate_cent = 566800,
            status = 'AVAILABLE',
            approved = True,
            approval_body = "DTCP"
        )
        self.data = [
            {
                "id" : self.site1.id,
                "name" : "test-site-1",
                "description" : "test description one",
                "owner_id" : self.owner.id,
                "owner_name" : self.owner.company_name,
                "located_at" : "test locality one",
                "latitude" : 11.1111,
                "longitude" : 12.1212,
                "area_sqft" : 100000.0,
                "area_cents" : 229.0,
                "total_properties" : 100,
                "properties_occupied" : 50,
                "properties_available" : 50,
                "land_rate_sqft" : 1300,
                "land_rate_cent" : 566800,
                "status" : 'AVAILABLE',
                "approved" : True,
                "approval_body" : "DTCP",
                "images" : []
            },
            {
                "id" : self.site2.id,
                "name" : "test-site-2",
                "description" : "test description two",
                "owner_id" : self.owner.id,
                "owner_name" : self.owner.company_name,
                "located_at" : "test locality two",
                "latitude" : 11.1111,
                "longitude" : 12.1212,
                "area_sqft" : 100000.0,
                "area_cents" : 229.0,
                "total_properties" : 100,
                "properties_occupied" : 50,
                "properties_available" : 50,
                "land_rate_sqft" : 1300,
                "land_rate_cent" : 566800,
                "status" : 'AVAILABLE',
                "approved" : True,
                "approval_body" : "DTCP",
                "images" : []
            }
        ]

    def test_sites_list_view(self):
        response = self.client.get(reverse('sites-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
                json.loads(response.content),
                self.data
            )