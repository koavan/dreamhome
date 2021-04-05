from rest_framework import serializers
from proprepo.models.site import Site
from proprepo.serializers.site_image import SiteImageSerializer

class SiteSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True)
    owner_name = serializers.SerializerMethodField('get_owner_name')

    def get_owner_name(self, site):
        return site.owner_id.company_name
    
    images = SiteImageSerializer(many=True, read_only=True)
    class Meta:
        model = Site
        fields = '__all__'