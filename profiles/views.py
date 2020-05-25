from rest_framework import ( generics, mixins)
from django.contrib.auth.models import User
from .models import Owner
from .serializers import ( OwnerSerializer, UserSerializer, )

# Owner related views
class OwnerListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetailAPIView(generics.RetrieveAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

# User related views
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer