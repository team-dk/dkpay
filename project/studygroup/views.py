from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
import random
import string
# Create your views here.
from django.views.generic import ListView
from django.views.generic import TemplateView

from studygroup.models import StudyGroup

chars = string.ascii_lowercase + string.digits

def index(request):
    return render(request, 'index.html')


def test(request):
    return HttpResponse(request, "hello world")


class LoginView(TemplateView):
    model = User
    template_name = 'login.html'


@login_required
class MainView(TemplateView):
    template_name = 'mygroups.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        study_groups = StudyGroup.objects.filter(user=self.request.user)
        context['group'] = study_groups
        return context


@login_required
def group_create(request):
    if request.method == "GET":
        return render(request, 'create-group.html')

    if request.method == "POST":
        group_name = request.POST.get('name')
        passcode = ''.join(random.choice(chars) for _ in range(8))

        group = StudyGroup(name=group_name,
                           passcode=passcode)
        group.save()
        group_id = group.id
