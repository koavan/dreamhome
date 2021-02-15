from rest_framework import generics
from proprepo.models import Property, PropertyImage
from proprepo.serializers import PropertyImageSerializer
from proprepo.permissions import IsOwnerOfProperty
from rest_framework.permissions import IsAuthenticated

class PropertyImageCreateAPIView(generics.CreateAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [ IsAuthenticated, IsOwnerOfProperty ]

    def perform_create(self, serializer):
        property_pk = self.kwargs.get('property_pk')
        property = generics.get_object_or_404(Property, pk=property_pk)
        serializer.save(property=property)