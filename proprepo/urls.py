from rest_framework.routers import DefaultRouter
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import (OwnerListCreateAPIView, OwnerDetailAPIView,
                    SiteListAPIView, SiteCreateAPIView, SiteDetailView,
                    SiteImageViewset,)

router = DefaultRouter()
router.register('',SiteImageViewset)

urlpatterns = [
    path('owners/', OwnerListCreateAPIView.as_view(), name='owners-list'),
    path('owners/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner-detail'),
    path('owners/<int:owner_pk>/site/', SiteCreateAPIView.as_view(), name='add-site'),
    path('sites/', SiteListAPIView.as_view(), name='sites-list'),
    path('sites/<int:pk>/', SiteDetailView.as_view(), name='site-detail'),
    path('site-images/', include(router.urls))
]
    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
