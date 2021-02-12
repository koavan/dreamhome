from django.contrib.admin.sites import site
from rest_framework import serializers
from .models import Owner, Site, Property, SiteImage, PropertyImage
from profiles.serializers.serializers import OwnerSerializer

class SiteImageSerializer(serializers.ModelSerializer):
    site = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = SiteImage
        fields = '__all__'

class SiteSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True)

    owner_name = serializers.SerializerMethodField('get_owner_name')

    def get_owner_name(self, site):
        return site.owner_id.company_name
    
    images = SiteImageSerializer(many=True, read_only=True)
    class Meta:
        model = Site
        fields = '__all__'

class PropertyImageSerializer(serializers.ModelSerializer):
    property = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = PropertyImage
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    site_id = serializers.PrimaryKeyRelatedField(read_only=True)
    images = PropertyImageSerializer(many=True, read_only=True)

    # custom fields
    owner_id = serializers.SerializerMethodField('get_owner_id')
    owner_name = serializers.SerializerMethodField('get_owner_name')
    site_name = serializers.SerializerMethodField('get_site_name')

    def get_owner_id(self, prop):
        return prop.site_id.owner_id.id

    def get_owner_name(self, prop):
        return prop.site_id.owner_id.company_name

    def get_site_name(self, prop):
        return prop.site_id.name

    class Meta:
        model = Property
        fields = '__all__'
