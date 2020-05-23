from rest_framework import ( generics, mixins)
from django.shortcuts import render
from rest_framework import viewsets
from .models import Owner, Site, Property, SiteImage
from .serializers import OwnerSerializer, SiteSerializer, PropertySerializer, SiteImageSerializer

class OwnerListCreateAPIView(generics.ListCreateAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetailAPIView(generics.RetrieveAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class SiteListAPIView(generics.ListAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteDetailView(generics.RetrieveAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

class SiteCreateAPIView(generics.CreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer

    def perform_create(self, serializer):
        owner_pk = self.kwargs.get('owner_pk')
        owner = generics.get_object_or_404(Owner, pk=owner_pk)
        serializer.save(owner_id = owner)

class SiteImageViewset(viewsets.ModelViewSet):
    queryset = SiteImage.objects.all()
    serializer_class = SiteImageSerializer

class PropertyViewset(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
