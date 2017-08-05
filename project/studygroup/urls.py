from django.conf.urls import url

from . import views
from .views import MainView

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', MainView.as_view(), name='home'),
    # url(r'^$', views.login, name='login'),
    url(r'^accept-invitation/$', views.accept_invite, name='accept_invite'),
    
    url(r'^create-session/$', views.create_session, name='create_session'),
    url(r'^edit-session/?P<id>[0-9]+/$', views.edit_session, name='edit_session'),
]