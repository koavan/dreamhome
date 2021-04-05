from rest_framework import serializers
from proprepo.models.property_image import PropertyImage

class PropertyImageSerializer(serializers.ModelSerializer):
    property = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = PropertyImage
        fields = '__all__'