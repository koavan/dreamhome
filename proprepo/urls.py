from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import (OwnerListCreateAPIView, OwnerDetailAPIView,
                    SiteListAPIView, SiteCreateAPIView, SiteDetailAPIView,
                    SiteImageCreateAPIView, SiteImageDetailAPIView,
                    PropertyListAPIView, PropertyCreateAPIView, PropertyDetailAPIView, 
                    FilteredPropertyListAPIView, PropertyImageDetailAPIView, 
                    PropertyImageCreateAPIView, )

urlpatterns = [
    path('owners/', OwnerListCreateAPIView.as_view(), name='owners-list'),
    path('owners/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner-detail'),
    path('owners/<int:owner_pk>/site/', SiteCreateAPIView.as_view(), name='add-site'),
    
    path('sites/', SiteListAPIView.as_view(), name='sites-list'),
    path('sites/<int:pk>/', SiteDetailAPIView.as_view(), name='site-detail'),
    path('sites/<int:site_pk>/image/', SiteImageCreateAPIView.as_view(), name='site-image-create'),
    path('sites/<int:site_pk>/property/', PropertyCreateAPIView.as_view(), name='property-add'),
    path('sites/<int:site_pk>/properties/', FilteredPropertyListAPIView.as_view(), name='list-properties'),
    
    path('site-images/<int:pk>/', SiteImageDetailAPIView.as_view(), name='site-image-detail'),
    
    path('properties/', PropertyListAPIView.as_view(), name='properties-list'),
    path('properties/<int:pk>/', PropertyDetailAPIView.as_view(), name='property-detail'),
    path('properties/<int:property_pk>/image/', PropertyImageCreateAPIView.as_view(), name='prop-image-create'),
    
    path('prop-images/<int:pk>/', PropertyImageDetailAPIView.as_view(), name='property-image-detail'),
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
