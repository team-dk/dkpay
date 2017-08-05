from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^home/$', views.test, name='home'),
    url(r'^login/$', views.login),
    url(r'^accept-invitation/$', views.accept_invite, name='accept_invite'),
]