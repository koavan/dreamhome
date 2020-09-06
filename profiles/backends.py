from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomAuthBackend(ModelBackend):

    def authenticate(self, request, **kwargs):
        # user_phone = kwargs['phone']
        user_phone = kwargs.get('phone', None)
        email = kwargs.get('email', None)
        password = kwargs['password']
        
        print(user_phone)
        print(email)
        print(password)
        try:
            if user_phone:
                print('Logging in with phone')
                user = User.objects.get(phone=user_phone)
            elif email:
                print('Logging in with email')
                user = User.objects.get(email=email)
                print(user)
            if user.check_password(password) is True:
                return user
        except User.DoesNotExist:
            pass