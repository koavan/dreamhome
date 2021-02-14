from django.http.response import HttpResponse
from rest_framework.response import Response
from rest_framework import ( generics, mixins)
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, status
from rest_framework.views import APIView
from .models import Site, Property, SiteImage, PropertyImage
from profiles.models import Owner
from .serializers import (  SiteSerializer, 
                            PropertySerializer, SiteImageSerializer, 
                            PropertyImageSerializer, )
from profiles.serializers import OwnerSerializer
from profiles.permissions import IsOwner
from .permissions import IsOwnerOfSite, IsOwnerOfProperty
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

# Site related views
class SiteListAPIView(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

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

class SiteCreateAPIView(generics.CreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [ IsAuthenticated, IsOwner ]

    def perform_create(self, serializer):
        user = generics.get_object_or_404(User, name=self.request.user)
        owner = user.owners
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
        filtered_data = Property.objects.filter(site_id__exact=site_pk).order_by('id')
        return filtered_data

class PropertyCreateAPIView(generics.CreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [ IsAuthenticated, IsOwner, IsOwnerOfSite ]

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
    permission_classes = [ IsAuthenticated, IsOwnerOfProperty ]

    def perform_create(self, serializer):
        property_pk = self.kwargs.get('property_pk')
        property = generics.get_object_or_404(Property, pk=property_pk)
        serializer.save(property=property)

class PropertyImageDetailAPIView(generics.RetrieveAPIView):
    queryset = PropertyImage.objects.all()
    serializer_class = PropertyImageSerializer

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