from django.conf.urls import url

from . import views
from .views import ProfileView
from .views import EditProfileView

urlpatterns = [
    url(r'^profile/',           ProfileView.as_view(),          name='profile'),
    url(r'^edit_profile/',     EditProfileView.as_view(),      name='edit_profile'),
]