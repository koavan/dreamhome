from django.db import models
from proprepo.models.site import Site

class SiteImage(models.Model):
    image = models.ImageField()
    site = models.ForeignKey(Site, on_delete=models.CASCADE, related_name='images')
    is_layout = models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = 'SiteImages'

    def __str__(self):
        return self.image.name