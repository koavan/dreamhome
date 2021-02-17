from django.db import models
from proprepo.models.site import Site

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

    class Meta:
        verbose_name_plural = 'Properties'

    def __str__(self):
        return self.name