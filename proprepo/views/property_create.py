from rest_framework import generics
from proprepo.models import Site, Property
from proprepo.serializers import PropertySerializer
from profiles.permissions.permissions import IsOwner
from proprepo.permissions import IsOwnerOfSite
from rest_framework.permissions import IsAuthenticated

class PropertyCreateAPIView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [ IsAuthenticated, IsOwner, IsOwnerOfSite ]

    def perform_create(self, serializer):
        site_pk = self.kwargs.get('site_pk')
        site = generics.get_object_or_404(Site, pk=site_pk)
        serializer.save(site_id=site)