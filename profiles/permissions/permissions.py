from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from profiles.models.buyer import Buyer
from django.contrib.auth import get_user_model

User = get_user_model()

class IsNoOwnerCreated(permissions.BasePermission):

    def has_permission(self, request, view):
        # print("inside IsNoOwnerCreated")
        has_owner = False
        user = get_object_or_404(User, name=request.user)
        try:
            temp = user.owners
            # print(temp)
            return False
        except ObjectDoesNotExist:
            # print("No owners existing for this user")
            return True

class IsOwner(permissions.BasePermission):

    def has_permission(self, request, view):
        # print("inside IsOwner")
        user = get_object_or_404(User, name=request.user)
        try:
            temp = user.owners
            # print(temp)
            if temp:
                return True
            return False
        except ObjectDoesNotExist:
            # print("No owners existing for this user")
            return False

class IsNoBuyerCreated(permissions.BasePermission):

    def has_permission(self, request, view):
        # print("inside IsNoBuyerCreated")
        has_owner = False
        user = get_object_or_404(User, name=request.user)
        try:
            temp = user.buyers
            # print(temp)
            return False
        except ObjectDoesNotExist:
            # print("No owners existing for this user")
            return True