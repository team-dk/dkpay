from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from django.views.generic import TemplateView

from dkpay.project.studygroup.models import StudyGroup


def index(request):
    return render(request, 'index.html')


def test(request):
    return HttpResponse(request, "hello world")


class LoginView(TemplateView):
    model = User
    template_name = 'login.html'


