import json
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from profiles.models.owner import Owner
from django.contrib.auth import get_user_model

User = get_user_model()

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
                "user":self.user.name,
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
            },
            msg='Able to see user detail'
        )