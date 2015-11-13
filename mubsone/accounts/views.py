from django.shortcuts import render
from .models import MubsoneUser
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
import json

# Create your views here.

class ProfileView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    def get(self, request):
        mUser = MubsoneUser.objects.get(user = request.user)
        data = {
            'username'      : request.user.username,
            'first_name'    : request.user.first_name,
            'last_name'     : request.user.last_name,
            'email'         : request.user.email,
            'fans'          : mUser.fans,
            'rating'        : mUser.rating,
            'biography'     : mUser.biography,
            'avatar'        : mUser.avatar,
            'videos'        : mUser.videos,
            'contests'      : mUser.contests,
            'is_premium'    : mUser.is_premium,
            'is_banned'     : mUser.is_banned
        }
        return Response(data)

class EditProfileView(APIView):
    permission_classes = (IsAuthenticated, )
    authentication_classes = (JSONWebTokenAuthentication, )

    parser_classes = (JSONParser, )

    def post(self, request, format=None):
        json_data = json.loads(request.body)
        print "JSON: "
        print json_data

        mUser = MubsoneUser.objects.get(user__username=request.user.username)
        print mUser.user.username
        print mUser.user.first_name
        # mUser.user.username = json_data["username"]
        mUser.user.first_name = json_data["first_name"]
        mUser.user.last_name = json_data["last_name"]
        mUser.biography = json_data["biography"]

        mUser.user.save()

        return Response(
            {
                "status" : "ok"

            }
        )