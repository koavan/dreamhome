from django.db import models
from proprepo.models.property import Property

class PropertyImage(models.Model):
    image = models.ImageField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    class Meta:
        verbose_name_plural = 'PropertyImages'

    def __str__(self):
        return self.image.name