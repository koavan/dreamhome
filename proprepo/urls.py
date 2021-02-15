from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from proprepo.views.site_list import SiteListAPIView
from proprepo.views.site_create import SiteCreateAPIView
from proprepo.views.site_detail import SiteDetailAPIView
from proprepo.views.siteImage_create import SiteImageCreateAPIView
from proprepo.views.siteImage_detail import SiteImageDetailAPIView
from proprepo.views.property_list import PropertyListAPIView
from proprepo.views.property_create import PropertyCreateAPIView
from proprepo.views.property_detail import PropertyDetailAPIView
from proprepo.views.property_list_filtered import FilteredPropertyListAPIView
from proprepo.views.propertyImage_detail import PropertyImageDetailAPIView
from proprepo.views.propertyImage_create import PropertyImageCreateAPIView
from proprepo.views.siteLayoutImage_detail import SiteLayoutImageDetailView

urlpatterns = [
    # path('owners/<int:owner_pk>/site/', SiteCreateAPIView.as_view(), name='add-site'),
    path('owners/site/', SiteCreateAPIView.as_view(), name='add-site'),

    path('sites/', SiteListAPIView.as_view(), name='sites-list'),
    path('sites/<int:pk>/', SiteDetailAPIView.as_view(), name='site-detail'),
    path('sites/<int:site_pk>/image/', SiteImageCreateAPIView.as_view(), name='site-image-create'),
    path('sites/<int:site_pk>/property/', PropertyCreateAPIView.as_view(), name='property-add'),
    path('sites/<int:site_pk>/properties/', FilteredPropertyListAPIView.as_view(), name='list-properties'),
    path('sites/<int:site_pk>/layout/', SiteLayoutImageDetailView.as_view(), name='site-layout'),

    path('site-images/<int:pk>/', SiteImageDetailAPIView.as_view(), name='site-image-detail'),
    
    path('properties/', PropertyListAPIView.as_view(), name='properties-list'),
    path('properties/<int:pk>/', PropertyDetailAPIView.as_view(), name='property-detail'),
    path('properties/<int:property_pk>/image/', PropertyImageCreateAPIView.as_view(), name='prop-image-create'),
    
    path('prop-images/<int:pk>/', PropertyImageDetailAPIView.as_view(), name='property-image-detail'),
]
