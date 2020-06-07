from rest_framework import ( generics, mixins)
from .models import Owner, Buyer
from .serializers import ( OwnerSerializer, UserSerializer, BuyerSerializer, )
from .permissions import IsNoOwnerCreated, IsNoBuyerCreated

from django.contrib.auth import get_user_model
from django.core.exceptions import ( ObjectDoesNotExist, ValidationError, )

from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

User = get_user_model()

# Owner related views
class OwnerListAPIView(generics.ListCreateAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetailAPIView(generics.RetrieveAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerCreateAPIView(generics.CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
    permission_classes = [ IsAuthenticated, IsNoOwnerCreated ]

    def perform_create(self, serializer):
        user = get_object_or_404(User, email=self.request.user)
        print(user.email)

        try:
            owners = user.owners
            print(owners)
            raise ValidationError("This user is already associated with a owner!")
        except ObjectDoesNotExist:
            # print("No owners existing for this user")
            serializer.save(user=user)

class BuyerCreateAPIView(generics.CreateAPIView):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
    permission_classes = [ IsAuthenticated, IsNoBuyerCreated ]

    def perform_create(self, serializer):
        user = get_object_or_404(User, email=self.request.user)
        print(user.email)

        try:
            buyers = user.owners
            print(buyers)
            raise ValidationError("This user is already associated with a owner!")
        except ObjectDoesNotExist:
            print("No owners existing for this user")
            serializer.save(user=user)