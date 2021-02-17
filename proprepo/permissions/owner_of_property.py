from rest_framework import permissions
from rest_framework.generics import get_object_or_404
# from .models import Property, Site
from proprepo.models.property import Property
from django.contrib.auth import get_user_model

User = get_user_model()

class IsOwnerOfProperty(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user:
            return False
        user = get_object_or_404(User, name=request.user)
        property_pk = view.kwargs.get('property_pk', None)
        # print(f'Property ID : { property_pk }')
        property = get_object_or_404(Property, id=property_pk)
        # print(property.name)
        # print(property.site_id.owner_id)
        
        # print(user.owners.company_name)
        
        if str(user.owners.company_name) == str(property.site_id.owner_id) :
            return True
        return False