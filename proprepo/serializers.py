from django.contrib.admin.sites import site
from rest_framework import serializers
from .models import Owner, Site, Property, SiteImage, PropertyImage
from profiles.serializers import OwnerSerializer

class SiteImageSerializer(serializers.ModelSerializer):
    site = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = SiteImage
        fields = '__all__'

class SiteSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True)
    
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

    owner_id = serializers.SerializerMethodField('get_owner_id')

    def get_owner_id(self, prop):
        owner = prop.site_id.owner_id.id
        print(owner)
        return owner

    class Meta:
        model = Property
        fields = '__all__'
