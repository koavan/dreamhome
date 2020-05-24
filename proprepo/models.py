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

class Site(models.Model):
    SITE_STATUS = [
        ('AVAILABLE', 'AVAILABLE'),
        ('NOT-AVAILABLE', 'NOT-AVAILABLE')
    ]
    APPROVAL_BODIES = [
        ('PANCHAYAT', 'PANCHAYAT'),
        ('DTCP', 'DTCP')
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True, null=True)
    owner_id = models.ForeignKey(Owner, on_delete=models.CASCADE)
    located_at = models.TextField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    area_sqft = models.FloatField()
    area_cents = models.FloatField()
    total_properties = models.IntegerField()
    properties_occupied = models.IntegerField(blank=True, null=True)
    properties_available = models.IntegerField()
    land_rate_sqft = models.BigIntegerField()
    land_rate_cent = models.BigIntegerField()
    status = models.CharField(max_length=30, choices=SITE_STATUS)
    approved = models.BooleanField(default=False)
    approval_body = models.CharField(max_length=20, choices=APPROVAL_BODIES, blank=True, null=True)
    # layout_image = models.ManyToManyField(SiteImage)

    class Meta:
        verbose_name_plural = 'Sites'

    def __str__(self):
        return self.name

class SiteImage(models.Model):
    image = models.ImageField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='images')
    class Meta:
        verbose_name_plural = 'SiteImages'

    def __str__(self):
        return self.image.name

class Property(models.Model):
    PROPERTY_TYPES = [
        ('LAND-APPROVED', 'LAND-APPROVED'),
        ('LAND-UNAPPROVED', 'LAND-UNAPPROVED'),
        ('BUILDING', 'BUILDING')
    ]
    PROPERTY_STATUS = [
        ('AVAILABLE', 'AVAILABLE'),
        ('NOT-AVAILABLE', 'NOT-AVAILABLE'),
        ('NOT-FOR-SALE', 'NOT-FOR-SALE'),
        ('SOLD', 'SOLD')
    ]
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=50, choices=PROPERTY_TYPES)
    site_id = models.ForeignKey(Site, on_delete=models.CASCADE)
    area_sqft = models.FloatField()
    area_cents = models.FloatField()
    facing_direction = models.CharField(max_length=30)
    land_rate_sqft = models.FloatField()
    land_rate_cent = models.FloatField()
    status = models.CharField(max_length=30, choices=PROPERTY_STATUS)
    # layout_image = models.ImageField()

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name
