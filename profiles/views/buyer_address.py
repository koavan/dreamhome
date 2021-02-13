from django.http import request
from django.http.response import HttpResponse
from rest_framework import ( generics, mixins)
from rest_framework import serializers
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from profiles.models.owner import Owner
from profiles.models.buyer import Buyer
from profiles.serializers.owner import OwnerSerializer
from profiles.serializers.user import UserSerializer
from profiles.serializers.buyer import BuyerSerializer
from profiles.permissions.permissions import IsNoOwnerCreated, IsNoBuyerCreated

from django.contrib.auth import get_user_model
from django.core.exceptions import ( ObjectDoesNotExist, ValidationError, )

from rest_framework import status, authentication
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.authtoken.models import Token

User = get_user_model()

# Owner related views
class BuyerAddressView(APIView):

    permission_classes = ( IsAuthenticated, )

    def post(self, request, *args, **kwargs):
        print('Buyer Address View')

        try:
            buyer = request.user.buyers

            print('Saving new address')
            buyer.address = request.POST.get('address', buyer.address)
            buyer.district = request.POST.get('district', buyer.district)
            buyer.state = request.POST.get('state', buyer.state)
            buyer.save()
        except User.buyers.RelatedObjectDoesNotExist:
            print(f'User { request.user } doesnt have associated buyer')
            print('Creating new buyer')

            buyer = Buyer()
            buyer.user = request.user
            buyer.address = request.POST.get('address', buyer.address)
            buyer.district = request.POST.get('district', buyer.district)
            buyer.state = request.POST.get('state', buyer.state)
            buyer.save()
        return Response({
            'success' : True,
            'message' : f'Buyer created for user { request.user }'
        }, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        print('Buyer Address View - GET')

        try:
            buyer = request.user.buyers
        except User.buyers.RelatedObjectDoesNotExist:
            print(f'User { request.user } doesnt have associated buyer')
            return Response({
                'success' : False,
                'message' : f'User { request.user } doesnt have associated buyer'
            }, status=status.HTTP_404_NOT_FOUND)
        else:
            payload = {
                "address" : buyer.address,
                "district" : buyer.district,
                "state" : buyer.state
            }
            return Response(payload, status=status.HTTP_200_OK)