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

class BuyerCreateAPIView(generics.CreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [ IsAuthenticated, IsNoBuyerCreated ]

    def perform_create(self, serializer):
        # print(self.request.user)
        user = get_object_or_404(User, name=self.request.user)

        try:
            buyers = user.buyers
            raise ValidationError("This user is already associated with a owner!")
        except ObjectDoesNotExist:
            # print("No owners existing for this user")
            serializer.save(user=user)