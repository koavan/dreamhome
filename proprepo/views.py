from rest_framework.response import Response
from rest_framework import ( generics, mixins)
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets
from .models import Site, Property, SiteImage, PropertyImage
from profiles.models import Owner
from .serializers import (  SiteSerializer, 
                            PropertySerializer, SiteImageSerializer, 
                            PropertyImageSerializer, )
from profiles.serializers import OwnerSerializer
from profiles.permissions import IsOwner
from .permissions import IsOwnerOfSite
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

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
    permission_classes = [ IsAuthenticated, IsOwner ]

    def perform_create(self, serializer):
        user = generics.get_object_or_404(User, email=self.request.user)
        owner = user.owners
        # print(owner.company_name)
        # owner = generics.get_object_or_404(Owner, email=self.request.user)
        serializer.save(owner_id = owner)

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
        # serializer.save(site=site)

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
    permission_classes = [ IsAuthenticated, IsOwnerOfSite ]

    def perform_create(self, serializer):
        site_pk = self.kwargs.get('site_pk')
        site = generics.get_object_or_404(Site, pk=site_pk)
        serializer.save(site_id=site)

class PropertyDetailAPIView(generics.RetrieveAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

# PropertyImage related views
class PropertyImageCreateAPIView(generics.CreateAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer
    permission_classes = [ IsAuthenticated, IsOwnerOfSite ]

    def perform_create(self, serializer):
        property_pk = self.kwargs.get('property_pk')
        property = generics.get_object_or_404(Property, pk=property_pk)
        serializer.save(property=property)

class PropertyImageDetailAPIView(generics.RetrieveAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer