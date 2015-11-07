from django.shortcuts import render
from .models import MubsoneUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import LoginForm, RegisterForm, ChangePasswordForm, EditProfileForm
# Create your views here.

def login_view(request):
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return JsonResponse(
                        {
                            "status" : "ok"
                        }
                    )
                else:
                    return JsonResponse(
                        {
                            "status" : "error",
                            "reason" : "Account has not been activated."
                        }
                    )
            else:
                return JsonResponse(
                    {
                        "status" : "error",
                        "reason" : "Wrong username or password."
                    }
                )
    if request.method == "GET":
        login_form = LoginForm()
        return render(request, 'accounts/login.html', {'form' : login_form})


@login_required
def profile(request):
    if request.method == 'GET':
        user = get_object_or_404(MubsoneUser, user=request.user)
        return JsonResponse(
            {
                "username"      : user.user.username,
                "first_name"    : user.user.first_name,
                "last_name"     : user.user.last_name,
                "email"         : user.user.last_name,
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

@login_required
def logout_view(request):
    logout(request)
    return JsonResponse(
        {
            "status" : "ok"
        }
    )

def register(request):
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username    = register_form.cleaned_data.get('username')
            password    = register_form.cleaned_data.get('password')
            email       = register_form.cleaned_data.get('email')
            if MubsoneUser.objects.filter(user__username=username).exists():
                return JsonResponse(
                    {
                        "status" : "error",
                        "reason" : "Username already exists."
                    }
                )
            elif MubsoneUser.objects.filter(user__email=email).exists():
                return JsonResponse(
                    {
                        "status" : "error",
                        "reason" : "Email already exists."
                    }
                )
            else:
                user = User.objects.create_user(username=username, password=password, email=email)
                user.save()
                mubsoneUser = MubsoneUser(user=user,
                                          rating=0,
                                          fans=0,
                                          biography='',
                                          avatar='',
                                          videos=0,
                                          contests=0,
                                          is_banned=False,
                                          is_premium=False)
                mubsoneUser.save()
                return JsonResponse(
                    {
                        "status" : "ok"
                    }
                )
    elif request.method == "GET":
        register_form = RegisterForm()
        return render(request, 'accounts/register.html', {'form': register_form})

@login_required
def change_password(request):
    if request.method == "POST":
        change_password_form = ChangePasswordForm(request.POST)
        if change_password_form.is_valid():
            old_password = change_password_form.cleaned_data.get('old_password')
            new_password = change_password_form.cleaned_data.get('new_password')
            user = authenticate(username=request.user.username, password=old_password)
            if user is not None:
                user.set_password(new_password)
                user.save()
                return JsonResponse(
                    {
                        "status" : "ok"
                    }
                )
            else:
                return JsonResponse(
                    {
                        "status" : "error",
                        "reason" : "Wrong old password."
                    }
                )
    elif request.method == "GET":
        change_password_form = ChangePasswordForm()
        return render(request, 'accounts/change_password.html', {'form': change_password_form})

@login_required
def edit_profile(request):
    if request.method == "POST":
        edit_profile_form = EditProfileForm(request.POST)
        if edit_profile_form.is_valid():
            username    = edit_profile_form.cleaned_data.get('username')
            first_name  = edit_profile_form.cleaned_data.get('first_name')
            last_name   = edit_profile_form.cleaned_data.get('last_name')
            biography   = edit_profile_form.cleaned_data.get('biography')

            user                    = MubsoneUser.objects.get(user=request.user)

            user.biography          = biography
            user.user.username      = username
            user.user.first_name    = first_name
            user.user.last_name     = last_name

            user.save()
            user.user.save()

            return JsonResponse(
                {
                    "status" : "ok"
                }
            )
    elif request.method == "GET":
        edit_profile_form = EditProfileForm()
        return render(request, 'accounts/edit_profile.html', {'form': edit_profile_form})