from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import ( OwnerListAPIView, OwnerDetailAPIView, OwnerCreateAPIView,
                     BuyerCreateAPIView, WhoamiAPIView, )

urlpatterns = [
    path('owners/', OwnerListAPIView.as_view(), name='owners-list'),
    path('owners/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner-detail'),
    path('owners/create/', OwnerCreateAPIView.as_view(), name='create-owner'),
    path('buyers/create/', BuyerCreateAPIView.as_view(), name='create-buyer'),
    path('whoami/', WhoamiAPIView.as_view(), name='who-am-i'),
]
