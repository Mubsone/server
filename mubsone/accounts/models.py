from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_activated
from django.dispatch import receiver
# Create your models here.


class MubsoneUser(models.Model):
    user = models.OneToOneField(User)
    rating = models.FloatField(default=0.0)
    fans = models.IntegerField(default=0)
    biography = models.TextField(max_length=256)
    avatar = models.CharField(max_length=64)
    videos = models.IntegerField(default=0)
    contests = models.IntegerField(default=0)
    is_banned = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)

    def natural_key(self):
        return self.user.natural_key()
    natural_key.dependencies = ['django.contrib.auth.models.User']

    def __str__(self):
        return self.user.username

@receiver(user_activated)
def registerMubsoneUser(sender, user, request, **kwargs):
    mUser = MubsoneUser(user=user, rating=0, fans=0, biography='', avatar='', is_banned=False, is_premium=False)
    mUser.save()