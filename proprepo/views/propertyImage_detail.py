from rest_framework import generics
from proprepo.models import PropertyImage
from proprepo.serializers import PropertyImageSerializer

class PropertyImageDetailAPIView(generics.RetrieveAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer