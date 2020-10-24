from django.http import request
from rest_framework import ( generics, mixins)
from rest_framework import serializers
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from .models import Owner, Buyer
from .serializers import ( OwnerSerializer, UserSerializer, BuyerSerializer, )
from .permissions import IsNoOwnerCreated, IsNoBuyerCreated

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
class OwnerListAPIView(generics.ListAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetailAPIView(generics.RetrieveAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerCreateAPIView(generics.CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [ IsAuthenticated, IsNoOwnerCreated, IsNoBuyerCreated ]

    def perform_create(self, serializer):
        # print(self.request.user)
        user = get_object_or_404(User, name=self.request.user)

        try:
            owners = user.owners
            raise ValidationError("This user is already associated with a owner!")
        except ObjectDoesNotExist:
            # print("No owners existing for this user")
            serializer.save(user=user)

class BuyerCreateAPIView(generics.CreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [ IsAuthenticated, IsNoBuyerCreated, IsNoOwnerCreated ]

    def perform_create(self, serializer):
        # print(self.request.user)
        user = get_object_or_404(User, name=self.request.user)

        try:
            buyers = user.owners
            raise ValidationError("This user is already associated with a owner!")
        except ObjectDoesNotExist:
            # print("No owners existing for this user")
            serializer.save(user=user)

class WhoamiAPIView(APIView):
    """
    API endpoint to get details of the current authenticated user.
    """

    def post(self, request, *args, **kwargs):
        """
        API endpoint to get details of the current authenticated user. Pass the authentication token in the header. It will get the user, buyer/owner details of the user logged in with the auth token passed in the header.
        """
        token = request.data.get('token', None)
        
        if token:
            who = {}
            user = get_object_or_404(Token, key=token).user
            # print(user.email)
            owner = None
            buyer = None

            try:
                owner = user.owners
                owner = OwnerSerializer(owner).data
                # print(owner)
                who['owner'] = owner
            except ObjectDoesNotExist:
                pass
            
            try:
                buyer = user.buyers
                buyer = BuyerSerializer(buyer).data
                # print(buyer)
                who['buyer'] = buyer
            except ObjectDoesNotExist:
                pass

            user_serializer = UserSerializer(user)
            who['user'] = user_serializer.data
            # print(who)
            return Response(who,status=HTTP_200_OK)

        return Response({'success':False, 'message':'None authenticated'},HTTP_400_BAD_REQUEST)