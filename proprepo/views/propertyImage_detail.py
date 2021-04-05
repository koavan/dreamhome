from rest_framework import generics
from proprepo.models.property_image import PropertyImage
# from proprepo.models import PropertyImage
from proprepo.serializers.property_image import PropertyImageSerializer

class PropertyImageDetailAPIView(generics.RetrieveAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer