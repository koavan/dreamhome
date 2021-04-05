from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from profiles.models.user import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='owners')
    company_name = models.CharField(max_length=100, unique=True, blank=False)
    address = models.TextField(max_length=255)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gstin = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=10, unique=True, blank=False)
    support_email_id = models.EmailField()
    website = models.URLField()
    pan_number = models.CharField(max_length=50)
    avatar = models.ImageField(blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Owners'

    def __str__(self):
        return self.company_name