from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from profiles.models.owner import Owner
from profiles.models.buyer import Buyer
from django.contrib.auth import get_user_model, authenticate
from django.utils.translation import ugettext_lazy as _
from django.conf import settings
from phonenumber_field.phonenumber import PhoneNumber
from phonenumber_field.serializerfields import PhoneNumberField

from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode as uid_decoder
from django.utils.encoding import force_text

from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from allauth.utils import ( email_address_exists, get_username_max_length )

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    # username = serializers.CharField(required=False, allow_blank=True)
    phone = PhoneNumberField(required=False, allow_blank=True )
    # phone = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'})

    def authenticate(self, **kwargs):
        return authenticate(self.context['request'], **kwargs)

    def _validate_email(self, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        else:
            msg = _('Must include "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_phone(self, phone, password):
        user = None

        if phone and password:
            user = self.authenticate(phone=phone, password=password)
        else:
            msg = _('Must include "phone" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def _validate_phone_email(self, phone, email, password):
        user = None

        if email and password:
            user = self.authenticate(email=email, password=password)
        elif phone and password:
            user = self.authenticate(phone=phone, password=password)
        else:
            msg = _('Must include either "phone" or "email" and "password".')
            raise exceptions.ValidationError(msg)

        return user

    def validate(self, attrs):
        phone = attrs.get('phone')
        phone = str(phone)
        # print(str(phone))
        email = attrs.get('email')
        password = attrs.get('password')

        user = None

        if 'allauth' in settings.INSTALLED_APPS:
            from allauth.account import app_settings

            # Authentication through email
            if app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.EMAIL:
                user = self._validate_email(email, password)

            # Authentication through username
            # elif app_settings.AUTHENTICATION_METHOD == app_settings.AuthenticationMethod.USERNAME:
            elif app_settings.AUTHENTICATION_METHOD == 'phone':
                # print(app_settings.AUTHENTICATION_METHOD)
                user = self._validate_phone(phone, password)

            # Authentication through either username or email
            else:
                user = self._validate_phone_email(phone, email, password)
                # print(user)

        else:
            # Authentication without using allauth
            if email:
                try:
                    username = UserModel.objects.get(email__iexact=email).get_username()
                except UserModel.DoesNotExist:
                    pass

            if username:
                user = self._validate_phone_email(phone, '', password)

        # Did we get back an active user?
        if user:
            if not user.is_active:
                msg = _('User account is disabled.')
                raise exceptions.ValidationError(msg)
        else:
            msg = _('Unable to log in with provided credentials.')
            raise exceptions.ValidationError(msg)

        # If required, is the email verified?
        if 'rest_auth.registration' in settings.INSTALLED_APPS:
            from allauth.account import app_settings
            if app_settings.EMAIL_VERIFICATION == app_settings.EmailVerificationMethod.MANDATORY:
                email_address = user.emailaddress_set.get(email=user.email)
                if not email_address.verified:
                    raise serializers.ValidationError(_('E-mail is not verified.'))

        attrs['user'] = user
        return attrs