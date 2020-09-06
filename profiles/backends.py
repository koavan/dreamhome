from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        user_phone = kwargs['phone']
        password = kwargs['password']
        try:
            user = User.objects.get(phone=user_phone)
            if user.check_password(password) is True:
                return user
        except User.DoesNotExist:
            pass