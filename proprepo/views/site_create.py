from rest_framework import generics
from django.contrib.auth import get_user_model
from proprepo.models.site import Site
# from proprepo.models import Site
from proprepo.serializers.site import SiteSerializer
from profiles.permissions.permissions import IsOwner
from rest_framework.permissions import IsAuthenticated

User = get_user_model()

class SiteCreateAPIView(generics.CreateAPIView):
    queryset = Site.objects.all()
    serializer_class = SiteSerializer
    permission_classes = [ IsAuthenticated, IsOwner ]

    def perform_create(self, serializer):
        user = generics.get_object_or_404(User, name=self.request.user)
        owner = user.owners
        serializer.save(owner_id = owner)