from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
from profiles.models.user import User

class Buyer(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='buyers')
	address = models.TextField(max_length=255)
	district = models.CharField(max_length=50)
	state = models.CharField(max_length=50)
	contact_number = models.CharField(max_length=10, unique=True, blank=False)
	avatar = models.ImageField(blank=True)
	created_at = models.DateField(auto_now_add=True)
	updated_at = models.DateField(auto_now=True)

	class Meta:
		verbose_name_plural = 'Buyers'
	
	def __str__(self):
		return self.user.name