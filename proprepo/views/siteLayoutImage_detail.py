from rest_framework.response import Response
from rest_framework import generics
from rest_framework import status
from proprepo.models import Site, SiteImage
from proprepo.serializers import SiteImageSerializer

class SiteLayoutImageDetailView(generics.RetrieveAPIView):
    serializer_class = SiteImageSerializer

    def retrieve(self, request, *args, **kwargs):
        site_id = self.kwargs.get('site_pk', None)
        site = generics.get_object_or_404(Site, pk=site_id)
        images = SiteImage.objects.filter(site__exact=site_id, is_layout__exact=True)
        if images.count()>0:
            serialized = self.get_serializer(images[0])
            return Response(serialized.data)
        return Response({
            'success': False,
            'message': 'No layout image found for this site'
        }, status=status.HTTP_404_NOT_FOUND)