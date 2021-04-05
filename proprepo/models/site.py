from django.db import models
from profiles.models.owner import Owner

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

    class Meta:
        verbose_name_plural = 'Sites'

    def __str__(self):
        return self.name