from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework_simplejwt.views import ( TokenObtainPairView, TokenRefreshView, )
from rest_framework.documentation import include_docs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('proprepo.urls')),
    path('profiles/', include('profiles.urls')),
    # path('auth/token/', TokenObtainPairView.as_view()),
    # path('auth/token/refresh/', TokenRefreshView.as_view())
    # path('api_auth/', include('rest_framework.urls')),
    path('rest_auth/', include('rest_auth.urls')),
    path('rest_auth/registration/', include('rest_auth.registration.urls')),
    path('docs/', include_docs_urls(title='dreamhome',description='backend of house-owner.in')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
