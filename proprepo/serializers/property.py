from rest_framework import serializers
from proprepo.models.property import Property
from proprepo.serializers.property_image import PropertyImageSerializer

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
