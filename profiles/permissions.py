from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import get_user_model

User = get_user_model()

class IsNoOwnerCreated(permissions.BasePermission):

    def has_permission(self, request, view):
        has_owner = False
        user = get_object_or_404(User, email=request.user)
        print("inside IsNoOwnerCreated")
        try:
            temp = user.owners
            print(temp)
            return False
        except ObjectDoesNotExist:
            print("No owners existing for this user")
            return True
        # return bool( request.user and request.user.is_authenticated() and has_owner )