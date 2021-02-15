from rest_framework import generics
from proprepo.models import SiteImage
from proprepo.serializers import SiteImageSerializer

class SiteImageDetailAPIView(generics.RetrieveAPIView):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer