from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Owner

@receiver(post_save, sender=User)
def create_owner(sender, instance, created, **kwargs):
    print('Created : ', created)
    if created:
        Owner.objects.create(user=instance)