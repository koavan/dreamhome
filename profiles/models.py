from django.db import models
from django.contrib.auth.models import User

class Owner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    address = models.TextField(max_length=255)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gstin = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    email_id = models.EmailField()
    website = models.URLField()
    pan_number = models.CharField(max_length=50)
    avatar = models.ImageField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Owners'

    def __str__(self):
        return self.user.username
