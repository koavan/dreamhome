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

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=get_username_max_length(),
        min_length=allauth_settings.USERNAME_MIN_LENGTH,
        required=allauth_settings.USERNAME_REQUIRED
    )
    phone = PhoneNumberField(required=False, allow_blank=True)
    # phone = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=allauth_settings.EMAIL_REQUIRED)
    password1 = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    def validate_username(self, username):
        username = get_adapter().clean_username(username)
        return username

    def validate_email(self, email):
        email = get_adapter().clean_email(email)
        if allauth_settings.UNIQUE_EMAIL:
            if email and email_address_exists(email):
                raise serializers.ValidationError(
                    _("A user is already registered with this e-mail address."))
        return email

    def validate_password1(self, password):
        return get_adapter().clean_password(password)

    def validate(self, data):
        if data['password1'] != data['password2']:
            raise serializers.ValidationError(_("The two password fields didn't match."))
        return data

    def custom_signup(self, request, user):
        pass

    def get_cleaned_data(self):
        # print(self.validated_data.get('phone'))
        return {
            'name': self.validated_data.get('username', ''),
            'password': self.validated_data.get('password1', ''),
            'email': self.validated_data.get('email', ''),
            'phone': str(self.validated_data.get('phone', '')),
        }

    def save(self, request):
        # adapter = get_adapter()
        # user = adapter.new_user(request)
        # self.cleaned_data = self.get_cleaned_data()
        # print(self.cleaned_data)
        # User.objects.create(**self.cleaned_data)
        # adapter.save_user(request, user, self)
        # self.custom_signup(request, user)
        # setup_user_email(request, user, [])

        self.cleaned_data = self.get_cleaned_data()
        # print(self.cleaned_data)
        password = self.cleaned_data.pop('password','')
        # print(password)
        user = User.objects.create(**self.cleaned_data)
        user.set_password(password)
        user.save()
        setup_user_email(request, user, [])
        return user