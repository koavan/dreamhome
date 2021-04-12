# from profiles.models.buyer import Buyer
# from profiles.models.user import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# @receiver(post_save, sender=User)
# def create_buyer(sender, instance, created, **kwargs):
#     print('Created : ', created)
#     if created:
#         Buyer.objects.create(user=instance)