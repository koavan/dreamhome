from rest_framework import generics
from proprepo.models import Site, SiteImage
from proprepo.serializers import SiteImageSerializer
from proprepo.permissions import IsOwnerOfSite
from rest_framework.permissions import IsAuthenticated

# Site Image related views
# class SiteImageListAPIView(viewsets.ModelViewSet):
#     queryset = SiteImage.objects.all()
#     serializer_class = SiteImageSerializer

class SiteImageCreateAPIView(generics.CreateAPIView):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer
    permission_classes = [ IsAuthenticated, IsOwnerOfSite ]

    def perform_create(self, serializer):
        site_pk = self.kwargs.get('site_pk')
        site = generics.get_object_or_404(Site, pk=site_pk)
        serializer.save(site=site)