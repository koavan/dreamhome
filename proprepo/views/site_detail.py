from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from proprepo.models import Site
from proprepo.serializers import SiteSerializer

class SiteDetailAPIView(generics.RetrieveAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def get_siteimage(self, image):
        image_as_dict = dict(image)
        if not image_as_dict.get('is_layout'):
            return dict(image)
        return None

    def retrieve(self, request, *args, **kwargs):
        site_detail = {}
        site_id = self.kwargs.get('pk')
        site = Site.objects.filter(pk=site_id)
        if site.count() > 0:
            site_serializer = self.get_serializer(site[0])
            images = list(map(self.get_siteimage, site_serializer.data.get('images')))
            images.remove(None) if None in images else images
            site_detail = {
                    **site_serializer.data, 
                    'images': images
                }
            return Response(site_detail, status=status.HTTP_200_OK)
        return Response({
            'success' : False,
            'message' : 'No such site exists'
        }, status=status.HTTP_404_NOT_FOUND)