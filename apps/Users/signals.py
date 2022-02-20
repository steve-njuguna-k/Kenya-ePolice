from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from apps.Users.models import OCSProfile, OfficerProfile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        OCSProfile.objects.create(user=instance)
        OfficerProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.ocsprofile.save()
    instance.officerprofile.save()