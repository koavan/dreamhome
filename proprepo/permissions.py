from rest_framework import permissions
from rest_framework.generics import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .models import Site
from django.contrib.auth import get_user_model

User = get_user_model()

class IsOwnerOfSite(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user:
            return False
        user = get_object_or_404(User, name=request.user)
        site_pk = view.kwargs.get('site_pk', None)
        # print(f'Site ID : { site_pk }')
        site = get_object_or_404(Site, id=site_pk)
        # print(site.name)
        # print(site.owner_id.company_name)
        
        # print(user.owners.company_name)
        
        if user.owners.company_name == site.owner_id.company_name :
            return True
        return False
