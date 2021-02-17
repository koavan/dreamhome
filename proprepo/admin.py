from django.contrib import admin
# from .models import Site, Property, SiteImage, PropertyImage
from proprepo.models.site import Site
from proprepo.models.site_image import SiteImage
from proprepo.models.property import Property
from proprepo.models.property_image import PropertyImage

admin.site.register(Site)
admin.site.register(Property)
admin.site.register(SiteImage)
admin.site.register(PropertyImage)