from django.conf.urls import url

from . import views
from .views import MainView

urlpatterns = [
    # url(r'^$', views.index, name='index'),
    url(r'^$', MainView.as_view(), name='home'),
    # url(r'^$', views.login, name='login'),
    url(r'^accept-invitation/$', views.accept_invite, name='accept_invite'),
    
]