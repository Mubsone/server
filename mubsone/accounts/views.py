from django.shortcuts import render
from .models import MubsoneUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from .serializers import MubsoneUserSerializer
from rest_framework import status

from .forms import LoginForm, RegisterForm, ChangePasswordForm, EditProfileForm


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

    def post(self, request, format=None):
        serializer = MubsoneUserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)