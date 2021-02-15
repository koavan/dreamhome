from rest_framework import generics
from proprepo.models import Property
from proprepo.serializers import PropertySerializer

class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer