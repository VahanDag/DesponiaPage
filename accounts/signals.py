from pages.models import Setting
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, UserRanks


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        UserRanks.objects.create(user=instance)
        Setting.objects.create(user=instance, name=f"{instance}")



@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if not instance.profile.image:
        instance.profile.image = "default.jpg"

    instance.profile.save()
