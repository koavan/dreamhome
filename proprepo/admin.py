from django.contrib import admin
from .models import Site, Property, Owner, SiteImage

admin.site.register(Site)
admin.site.register(Property)
admin.site.register(Owner)
admin.site.register(SiteImage)