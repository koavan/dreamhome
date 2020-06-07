from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

class UserManager(BaseUserManager):

  def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
    if not email:
        raise ValueError('Users must have an email address')
    now = timezone.now()
    email = self.normalize_email(email)
    user = self.model(
        email=email,
        is_staff=is_staff, 
        is_active=True,
        is_superuser=is_superuser, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_user(self, email, password, **extra_fields):
    return self._create_user(email, password, False, False, **extra_fields)

  def create_superuser(self, email, password, **extra_fields):
    user=self._create_user(email, password, True, True, **extra_fields)
    return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254, unique=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self):
        return "/users/%i/" % (self.pk)


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