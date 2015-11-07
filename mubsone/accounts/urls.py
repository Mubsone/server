from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/',           views.profile,          name='profile'),
    url(r'^login/',             views.login_view,       name='login'),
    url(r'^logout/',            views.logout_view,      name='logout'),
    url(r'^register/',          views.register,         name='register'),
    url(r'^password/change/',   views.change_password,  name='change_password'),
    url(r'^edit/',              views.edit_profile,     name='edit_profile'),
]