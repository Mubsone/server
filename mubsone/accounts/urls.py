from django.conf.urls import url

from .views import ProfileView
from .views import EditProfileView
from .views import RegisterView

urlpatterns = [
    url(r'^profile/',           ProfileView.as_view(),          name='profile'),
    url(r'^edit_profile/',      EditProfileView.as_view(),      name='edit_profile'),
    url(r'^register/',          RegisterView.as_view(),         name='register'),
]