from django.shortcuts import render
from rest_framework import viewsets
from .models import Owner, Site, Property, SiteImage
from .serializers import OwnerSerializer, SiteSerializer, PropertySerializer, SiteImageSerializer

class OwnerViewset(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class SiteViewset(viewsets.ModelViewSet):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class PropertyViewset(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

class SiteImageViewset(viewsets.ModelViewSet):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer

