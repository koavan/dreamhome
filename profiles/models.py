from django.db import models

class Owner(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=255)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    gstin = models.CharField(max_length=50)
    contact_number = models.CharField(max_length=50)
    email_id = models.EmailField()
    website = models.URLField()
    pan_number = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Owners'

    def __str__(self):
        return self.name
