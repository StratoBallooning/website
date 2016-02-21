from __future__ import unicode_literals

from django.db import models
from django.db.models.signals import post_save
from django.conf import settings


class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_profile')
    position = models.CharField(max_length=100, blank=True)
    organization = models.CharField(max_length=100, blank=True)
    website = models.URLField(blank=True)

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

post_save.connect(create_user_profile, sender=settings.AUTH_USER_MODEL)
