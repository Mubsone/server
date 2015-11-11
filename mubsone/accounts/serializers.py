from rest_framework import serializers
from .models import MubsoneUser
class MubsoneUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MubsoneUser
        fields = ('user', 'rating', 'fans', 'biography', 'avatar', 'videos', 'contests', 'is_banned', 'is_premium')