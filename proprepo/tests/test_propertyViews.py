from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
import json
from profiles.models import Owner, Buyer
from proprepo.models import Site, Property
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

User = get_user_model()

class PropertyCreateAPIViewTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='test@test.com', name='test')
        self.owner1 = Owner.objects.create(user=self.user1, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)
        self.site1 = Site.objects.create(
            name = "test-site",
            description = "test description",
            owner_id = self.owner1,
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

        self.token1 = Token.objects.create(user=self.user1)
        self.api_authentication(self.token1.key)
    
    def api_authentication(self, key):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + key )

    def test_property_creation_authenticated(self):
        payload = {
            "name" : "Plot no : 1",
            "description" : "East facing plot",
            "type" : "LAND-APPROVED",
            "area_sqft" : 760,
            "area_cents" : 1.75,
            "facing_direction" : "EAST",
            "land_rate_sqft" : 1300,
            "land_rate_cent" : 566800,
            "status" : "AVAILABLE"
        }
        data = {
            "id" : 1,
            "site_id" : self.site1.name,
            "images" : [],
            "name" : "Plot no : 1",
            "description" : "East facing plot",
            "type" : "LAND-APPROVED",
            "area_sqft" : 760.0,
            "area_cents" : 1.75,
            "facing_direction" : "EAST",
            "land_rate_sqft" : 1300.0,
            "land_rate_cent" : 566800.0,
            "status" : "AVAILABLE"
        }
        response = self.client.post(reverse('property-add', kwargs={'site_pk' : self.site1.id }), payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
                json.loads(response.content), 
                data
            )

    def test_property_creation_unauthenticated(self):
        self.client.force_authenticate(user=None)
        payload = {
            "name" : "Plot no : 1",
            "description" : "East facing plot",
            "type" : "LAND-APPROVED",
            "area_sqft" : 760,
            "area_cents" : 1.75,
            "facing_direction" : "EAST",
            "land_rate_sqft" : 1300,
            "land_rate_cent" : 566800,
            "status" : "AVAILABLE"
        }
        data = {
            "id" : 1,
            "site_id" : self.site1.name,
            "images" : [],
            "name" : "Plot no : 1",
            "description" : "East facing plot",
            "type" : "LAND-APPROVED",
            "area_sqft" : 760.0,
            "area_cents" : 1.75,
            "facing_direction" : "EAST",
            "land_rate_sqft" : 1300.0,
            "land_rate_cent" : 566800.0,
            "status" : "AVAILABLE"
        }
        response = self.client.post(reverse('property-add', kwargs={'site_pk' : self.site1.id }), payload)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(json.loads(response.content), {
                'detail': 'Authentication credentials were not provided.'
                }
            )

    def test_property_creation_authenticated_duplicate(self):
        payload1 = {
            "name" : "Plot no : 1",
            "description" : "East facing plot",
            "type" : "LAND-APPROVED",
            "area_sqft" : 760,
            "area_cents" : 1.75,
            "facing_direction" : "EAST",
            "land_rate_sqft" : 1300,
            "land_rate_cent" : 566800,
            "status" : "AVAILABLE"
        }
        data1 = {
            "id" : 2,
            "site_id" : self.site1.name,
            "images" : [],
            "name" : "Plot no : 1",
            "description" : "East facing plot",
            "type" : "LAND-APPROVED",
            "area_sqft" : 760.0,
            "area_cents" : 1.75,
            "facing_direction" : "EAST",
            "land_rate_sqft" : 1300.0,
            "land_rate_cent" : 566800.0,
            "status" : "AVAILABLE"
        }

        payload2 = {
            "name" : "Plot no : 2",
            "description" : "West facing plot",
            "type" : "LAND-APPROVED",
            "area_sqft" : 760,
            "area_cents" : 1.75,
            "facing_direction" : "WEST",
            "land_rate_sqft" : 1300,
            "land_rate_cent" : 566800,
            "status" : "AVAILABLE"
        }
        data2 = {
            "id" : 3,
            "site_id" : self.site1.name,
            "images" : [],
            "name" : "Plot no : 2",
            "description" : "West facing plot",
            "type" : "LAND-APPROVED",
            "area_sqft" : 760.0,
            "area_cents" : 1.75,
            "facing_direction" : "WEST",
            "land_rate_sqft" : 1300.0,
            "land_rate_cent" : 566800.0,
            "status" : "AVAILABLE"
        }

        response = self.client.post(reverse('property-add', kwargs={'site_pk' : self.site1.id }), payload1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
                json.loads(response.content), 
                data1
            )

        response = self.client.post(reverse('property-add', kwargs={'site_pk' : self.site1.id }), payload2)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(
                json.loads(response.content), 
                data2
            )

class PropertyDetailAPIViewTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create(email='test@test.com', name='test')
        self.owner1 = Owner.objects.create(user=self.user1, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)
        self.site1 = Site.objects.create(
            name = "test-site",
            description = "test description",
            owner_id = self.owner1,
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

        self.property1 = Property.objects.create(
            name = "Plot no : 1",
            description = "East facing plot",
            type = "LAND-APPROVED",
            site_id = self.site1,
            area_sqft = 760,
            area_cents = 1.75,
            facing_direction = "EAST",
            land_rate_sqft = 1300,
            land_rate_cent = 566800,
            status = "AVAILABLE"
        )
        
        self.data = {
            "id" : 4,
            "site_id" : self.site1.name,
            "images" : [],
            "name" : "Plot no : 1",
            "description" : "East facing plot",
            "type" : "LAND-APPROVED",
            "area_sqft" : 760.0,
            "area_cents" : 1.75,
            "facing_direction" : "EAST",
            "land_rate_sqft" : 1300.0,
            "land_rate_cent" : 566800.0,
            "status" : "AVAILABLE"
        }
        
    def test_site_detail_view(self):
        response = self.client.get(reverse('property-detail', kwargs={ 'pk' : self.property1.id }))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            json.loads(response.content),
            self.data
        )

class PropertyListAPIViewTest(APITestCase):
    url = reverse('properties-list')
    def setUp(self):
        self.user1 = User.objects.create(email='test@test.com', name='test')
        self.owner1 = Owner.objects.create(user=self.user1, company_name='test-company', address='test-address', 
            district='test-district', state='test-state',
            gstin='test-gstin', contact_number='9876543210',
            support_email_id='test@test.com', website='https://test.com',
            pan_number='ABCD1234EF', avatar=None)
        self.site1 = Site.objects.create(
            name = "test-site",
            description = "test description",
            owner_id = self.owner1,
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

        self.property1 = Property.objects.create(
            name = "Plot no : 1",
            description = "East facing plot",
            type = "LAND-APPROVED",
            site_id = self.site1,
            area_sqft = 760,
            area_cents = 1.75,
            facing_direction = "EAST",
            land_rate_sqft = 1300,
            land_rate_cent = 566800,
            status = "AVAILABLE"
        )
        
        self.property2 = Property.objects.create(
            name = "Plot no : 2",
            description = "West facing plot",
            type = "LAND-APPROVED",
            site_id = self.site1,
            area_sqft = 760,
            area_cents = 1.75,
            facing_direction = "WEST",
            land_rate_sqft = 1300,
            land_rate_cent = 566800,
            status = "AVAILABLE"
        )

        self.data = [
            {
                "id" : 5,
                "site_id" : self.site1.name,
                "images" : [],
                "name" : "Plot no : 1",
                "description" : "East facing plot",
                "type" : "LAND-APPROVED",
                "area_sqft" : 760.0,
                "area_cents" : 1.75,
                "facing_direction" : "EAST",
                "land_rate_sqft" : 1300.0,
                "land_rate_cent" : 566800.0,
                "status" : "AVAILABLE"
            },
            {
                "id" : 6,
                "site_id" : self.site1.name,
                "images" : [],
                "name" : "Plot no : 2",
                "description" : "West facing plot",
                "type" : "LAND-APPROVED",
                "area_sqft" : 760.0,
                "area_cents" : 1.75,
                "facing_direction" : "WEST",
                "land_rate_sqft" : 1300.0,
                "land_rate_cent" : 566800.0,
                "status" : "AVAILABLE"
            }
        ]

    def test_property_list_view(self):
        response = self.client.get(self.url)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )
        self.assertEqual(
            json.loads(response.content),
            self.data
        )