from rest_framework import generics
from proprepo.models.property import Property
# from proprepo.models import Property
from proprepo.serializers.property import PropertySerializer

class FilteredPropertyListAPIView(generics.ListAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        site_pk = self.kwargs.get('site_pk')
        filtered_data = Property.objects.filter(site_id__exact=site_pk).order_by('id')
        return filtered_data