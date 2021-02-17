from rest_framework import generics
from proprepo.models.property import Property
# from proprepo.models import Property
from proprepo.serializers.property import PropertySerializer

class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer