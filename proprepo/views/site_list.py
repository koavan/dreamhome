from rest_framework import generics
from proprepo.models.site import Site
# from proprepo.models import Site
from proprepo.serializers.site import SiteSerializer

class SiteListAPIView(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer