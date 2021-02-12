from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from profiles.models.models import Owner, Buyer
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

class OwnerSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Owner
        exclude = ('created_at', 'updated_at', )
        # fields = '__all__'

class BuyerSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Buyer
        exclude = ('created_at', 'updated_at', )
        # fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'phone', 'password', )
        read_only_fields = ( 'id', )
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

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