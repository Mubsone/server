from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class MubsoneUser(models.Model):
    user = models.OneToOneField(User)
    rating = models.IntegerField(default=0)
    fans = models.IntegerField(default=0)
    biography = models.TextField(max_length=256)
    is_banned = models.BooleanField(default=False)
    avatar = models.CharField(max_length=64)
    is_premium = models.BooleanField(default=False)

    def natural_key(self):
        return self.user.natural_key()
    natural_key.dependencies = ['django.contrib.auth.models.User']