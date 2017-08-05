from django.conf.urls import url

from . import views
from .views import MainView, Dashboard, Session

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', MainView.as_view(), name='home'),
    # url(r'^$', views.login, name='login'),
    url(r'^create-group/$', views.group_create, name='create_group'),
    url(r'^create-group/result', views.create_group_result, name='create_group_result'),
    url(r'^accept-invitation/$', views.accept_invite, name='accept_invite'),
    url(r'^dashboard/$', Dashboard.as_view(), name='dashboard'),
    url(r'^create-session/(?P<id>\d+)$', views.create_session, name='create_session'),
    url(r'^edit-session/(?P<id>[0-9]+)/$', views.edit_session, name='edit_session'),
    url(r'^dashboard/session/$', Session.as_view(), name='session_v2')

]