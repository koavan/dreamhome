from profiles.views.whoami import WhoamiAPIView
from profiles.views.buyer_address import BuyerAddressView
from profiles.views.buyer_create import BuyerCreateAPIView
from profiles.views.owner_create import OwnerCreateAPIView
from profiles.views.owner_list import OwnerListAPIView
from profiles.views.owner_detail import OwnerDetailAPIView
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('owners/', OwnerListAPIView.as_view(), name='owners-list'),
    path('owners/<int:pk>/', OwnerDetailAPIView.as_view(), name='owner-detail'),
    path('owners/create/', OwnerCreateAPIView.as_view(), name='create-owner'),
    path('buyers/create/', BuyerCreateAPIView.as_view(), name='create-buyer'),
    path('buyers/address/', BuyerAddressView.as_view(), name='buyer-address'),
    path('whoami/', WhoamiAPIView.as_view(), name='who-am-i'),
]
