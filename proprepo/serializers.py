from rest_framework import serializers
from .models import Owner, Site, Property, SiteImage

class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Owner
        fields = '__all__'

class SiteSerializer(serializers.ModelSerializer):
    owner_id = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Site
        # exclude = ('owner_id',)
        fields = '__all__'

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = '__all__'

class SiteImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteImage
        fields = '__all__'