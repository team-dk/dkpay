from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^accept-invitation/$', views.accept_invitation),
    url(r'^mygroups/$', views.my_groups),
    url(r'^create-group/$', views.create_group),
    url(r'^group-dashboard/$', views.group_dashboard),
]