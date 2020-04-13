from django.urls import path, include
from rest_framework import routers
from .views import OwnerViewset, SiteViewset, PropertyViewset, SiteImageViewset
from django.conf.urls.static import static
from django.conf import settings

router = routers.DefaultRouter()
router.register('sites', SiteViewset)
router.register('owners', OwnerViewset)
router.register('properties', PropertyViewset)
router.register('siteimages', SiteImageViewset)

urlpatterns = [
    path('', include(router.urls)),
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
