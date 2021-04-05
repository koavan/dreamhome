from rest_framework import generics
from proprepo.models.site_image import SiteImage
# from proprepo.models import SiteImage
from proprepo.serializers.site_image import SiteImageSerializer

class SiteImageDetailAPIView(generics.RetrieveAPIView):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer