from rest_framework.response import Response
from rest_framework import ( generics, mixins)
from django.shortcuts import render
from rest_framework import viewsets
from .models import Owner, Site, Property, SiteImage
from .serializers import OwnerSerializer, SiteSerializer, PropertySerializer, SiteImageSerializer

# Owner related views
class OwnerListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetailAPIView(generics.RetrieveAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

# Site related views
class SiteListAPIView(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteDetailAPIView(generics.RetrieveAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteCreateAPIView(generics.CreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def perform_create(self, serializer):
        owner_pk = self.kwargs.get('owner_pk')
        owner = generics.get_object_or_404(Owner, pk=owner_pk)
        serializer.save(owner_id = owner)

# Site Image related views
# class SiteImageListAPIView(viewsets.ModelViewSet):
#     queryset = SiteImage.objects.all()
#     serializer_class = SiteImageSerializer

class SiteImageCreateAPIView(generics.CreateAPIView):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer

    def perform_create(self, serializer):
        site_pk = self.kwargs.get('site_pk')
        site = generics.get_object_or_404(Site, pk=site_pk)
        serializer.save(site=site)

class SiteImageDetailAPIView(generics.RetrieveAPIView):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer

# Property related views
class PropertyListAPIView(generics.ListAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class FilteredPropertyListAPIView(generics.ListAPIView):
    serializer_class = PropertySerializer

    def get_queryset(self):
        site_pk = self.kwargs.get('site_pk')
        filtered_data = Property.objects.filter(site_id__exact=site_pk)
        return filtered_data

class PropertyCreateAPIView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def perform_create(self, serializer):
        site_pk = self.kwargs.get('site_pk')
        site = generics.get_object_or_404(Site, pk=site_pk)
        serializer.save(site_id=site)

class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer