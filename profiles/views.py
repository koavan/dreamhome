from rest_framework import ( generics, mixins)
from .models import Owner
from .serializers import ( OwnerSerializer, UserSerializer, )
from .permissions import IsNoOwnerCreated

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
        # print(self.request.user)
        # print(self.request.data)
        user = get_object_or_404(User, email=self.request.user)
        print(user.email)

        try:
            temp = user.owners
            print(temp)
            raise ValidationError("This user is already associated with a owner!")
        except ObjectDoesNotExist:
            print("No owners existing for this user")
            serializer.save(user=user)
