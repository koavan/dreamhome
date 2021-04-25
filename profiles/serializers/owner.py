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

class OwnerSerializer(serializers.ModelSerializer):
    # user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Owner
        exclude = ('created_at', 'updated_at', )
        # fields = '__all__'
        read_only_fields = ( 'user', )
