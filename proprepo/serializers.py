from rest_framework import serializers
from .models import Owner, Site, Property, SiteImage

class OwnerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Owner
        fields = ('id', 'url', 'name', 'address', 'district', 'state',
        'gstin', 'contact_number', 'email_id', 'website', 'pan_number' )

class SiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Site
        fields = (
            'id', 'url', 'name', 'description', 'owner_id', 'located_at', 
            'latitude', 'longitude', 'area_sqft', 'area_cents', 'total_properties', 
            'properties_occupied', 'properties_available', 'land_rate_sqft', 
            'land_rate_cent', 'status', 'approved', 'approval_body', 'layout_image',
        )

class PropertySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Property
        fields = (
            'id', 'url', 'name', 'description', 'type', 'site_id', 'area_sqft', 'area_cents', 
            'facing_direction', 'land_rate_sqft', 'land_rate_cent', 'status', 'layout_image', 
        )

class SiteImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SiteImage
        fields = (
            'id', 'url', 'image',
        )