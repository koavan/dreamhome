from rest_framework import ( generics, mixins)
from .models import Owner
from .serializers import ( OwnerSerializer, )

# Owner related views
class OwnerListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetailAPIView(generics.RetrieveAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer
