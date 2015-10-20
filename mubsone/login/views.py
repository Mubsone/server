from django.shortcuts import render, get_object_or_404
from .models import User

# Create your views here.
def login(request, uname, passw):
    u = get_object_or_404(User, username=uname, password=passw)
    return render(request, 'login/login.html', { 'u': u })
