from django.shortcuts import render
from .models import MubsoneUser
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .forms import LoginForm
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