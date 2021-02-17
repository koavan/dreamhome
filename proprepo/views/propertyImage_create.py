from rest_framework import generics
from proprepo.models.property import Property
from proprepo.models.property_image import PropertyImage
# from proprepo.models import Property
# from proprepo.models import PropertyImage
from proprepo.serializers.property_image import PropertyImageSerializer
from proprepo.permissions.owner_of_property import IsOwnerOfProperty
from rest_framework.permissions import IsAuthenticated

class PropertyImageCreateAPIView(generics.CreateAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [ IsAuthenticated, IsOwnerOfProperty ]

    def perform_create(self, serializer):
        property_pk = self.kwargs.get('property_pk')
        property = generics.get_object_or_404(Property, pk=property_pk)
        serializer.save(property=property)