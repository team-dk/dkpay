from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render
import random
import string
# Create your views here.
from django.template.response import TemplateResponse
from django.views.generic import ListView
from django.views.generic import TemplateView

from studygroup.models import StudyGroup, StudyGroupRule, StudyGroupMember,StudyGroupSession

chars = string.ascii_lowercase + string.digits


def index(request):
    return render(request, 'index.html')


def test(request):
    return HttpResponse(request, "hello world")


def login(request):
    return TemplateResponse(request, 'layout_login.html')
#
# class LoginView(TemplateView):
#     model = User
#     template_name = 'login.html'


@login_required
def accept_invitation(request):
    return TemplateResponse(request, 'layout_accept_invitation.html')


class LoginView(TemplateView):
    model = User
    template_name = 'layout_login.html'


@login_required
class MainView(TemplateView):
    template_name = 'layout_mygroups.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        study_groups = StudyGroup.objects.filter(user=self.request.user)
        context['group'] = study_groups
        return context


@login_required
def group_create(request):
    if request.method == "GET":
        return render(request, 'layout_create_group.html')

    elif request.method == "POST":
        group_name = request.POST.get('name')
        passcode = ''.join(random.choice(chars) for _ in range(8))

        group = StudyGroup(name=group_name,
                           passcode=passcode)
        group.save()
        group_id = group.id

        return HttpResponse(group.passcode)


@login_required
def accept_invite(request):
    if request.method == "GET":
        return render(request, 'layout_accept_invitation.html')

    elif request.method == "POST":
        passcode = request.POST.get('passcode')
        print(passcode)
        try:
            group = StudyGroup.objects.get(passcode=passcode)
        except:
            return HttpResponseNotFound('error')
        else:
            member = StudyGroupMember(
                user=request.user,
                group=group
            )
            member.save()

            # group_sessions = StudyGroupSession.objects.filter(study_group=group)
            g_id = str(group.id)
            return HttpResponse(g_id)


@login_required
def edit_group(request):
    if request.method == "GET":
        group_id = request.GET.get('id')
        group = StudyGroup.objects.get(id=group_id)
        return render(request, 'layout_edit_group.html', {'group':group})

