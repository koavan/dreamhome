from rest_framework import generics
from proprepo.models import Property
from proprepo.serializers import PropertySerializer

class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer