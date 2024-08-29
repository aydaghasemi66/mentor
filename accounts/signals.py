from django.db.models.signals import post_save
from .models import CustomeUser, Profile
from django.dispatch import receiver

@receiver(post_save, sender=CustomeUser)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()

@receiver(post_save, sender=Profile)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user = CustomeUser.objects.get(email=instance.user.email)
        user.is_verified = True
        user.save()