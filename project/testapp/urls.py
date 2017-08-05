from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^accept-invitation/$', views.accept_invitation),
]