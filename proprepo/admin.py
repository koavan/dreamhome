from django.contrib import admin
from .models import Site, Property, Owner, SiteImage, PropertyImage

admin.site.register(Site)
admin.site.register(Property)
admin.site.register(Owner)
admin.site.register(SiteImage)
admin.site.register(PropertyImage)