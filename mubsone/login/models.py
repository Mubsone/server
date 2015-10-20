from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    username = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    rating = models.IntegerField(default=0)
    fans = models.IntegerField(default=0)
    biography = models.CharField(max_length=200)
    is_banned = models.BooleanField(default=False)
    email = models.CharField(max_length=45)
    avatar = models.CharField(max_length=45)
    is_admin = models.BooleanField(default=False)
    is_premium = models.BooleanField(default=False)

    def __str__(self):
        return self.username