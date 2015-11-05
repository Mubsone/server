from django.shortcuts import render
from django.core import serializers
from .models import MubsoneUser
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponse
# Create your views here.


@login_required
def profile(request):
    if request.method == 'GET':
        user = get_object_or_404(MubsoneUser, user=request.user)
        return JsonResponse(
            {
                "username"      : user.user.username,
                "fans"          : user.fans,
                "rating"        : user.rating,
                "biography"     : user.biography,
                "avatar"        : user.avatar,
                "videos"        : user.videos,
                "contests"      : user.contests,
                "is_premium"    : user.is_premium,
                "is_banned"     : user.is_banned

             }



        )