from django.shortcuts import render
from django.core import serializers
from .models import MubsoneUser
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
# Create your views here.


@login_required
def profile(request):
    if request.method == 'GET':
        user = get_object_or_404(MubsoneUser, user=request.user)
        return JsonResponse(serializers.serialize('json', [ user, ], use_natural_foreign_keys=True, use_natural_primary_keys=True), safe=False)