from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import ( OwnerListCreateAPIView, OwnerDetailAPIView, UserCreateAPIView, )

urlpatterns = [
    path('owners/', OwnerListCreateAPIView.as_view(), name='owners-list'),
    path('owners/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner-detail'),
    path('register/', UserCreateAPIView.as_view(), name='create-user'),
]
