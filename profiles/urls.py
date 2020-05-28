from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import ( OwnerListAPIView, OwnerDetailAPIView, OwnerCreateAPIView,
                     UserCreateAPIView, )

urlpatterns = [
    path('owners/', OwnerListAPIView.as_view(), name='owners-list'),
    path('owners/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner-detail'),
    path('users/register/', UserCreateAPIView.as_view(), name='create-user'),
    # path('users/login/', ),
    path('users/<int:user_pk>/owner/', OwnerCreateAPIView.as_view(), name='create-owner'),
]
