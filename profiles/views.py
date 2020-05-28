from rest_framework import ( generics, mixins)
from .models import Owner
from .serializers import ( OwnerSerializer, UserSerializer, )
from django.contrib.auth import get_user_model
from rest_framework.generics import get_object_or_404

User = get_user_model()

# Owner related views
class OwnerListAPIView(generics.ListCreateAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerDetailAPIView(generics.RetrieveAPIView): 
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class OwnerCreateAPIView(generics.CreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

    def perform_create(self, serializer):
        user_pk = self.kwargs.get('user_pk')
        user = get_object_or_404(User, pk=user_pk)
        serializer.save(user=user)

# User related views
class UserCreateAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = ['rest_framework.permissions.AllowAny']

    def perform_authentication(self, request):
        return super().perform_authentication(request)