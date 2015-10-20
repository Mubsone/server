from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<uname>[a-zA-Z0-9]+)/(?P<passw>[a-z]+)$', views.login, name='login'),
]
