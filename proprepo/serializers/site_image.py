from rest_framework import serializers
from proprepo.models.site_image import SiteImage

class SiteImageSerializer(serializers.ModelSerializer):
    site = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = SiteImage
        fields = '__all__'
