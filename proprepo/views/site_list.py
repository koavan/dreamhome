from rest_framework import generics
from proprepo.models import Site
from proprepo.serializers import SiteSerializer

class SiteListAPIView(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer