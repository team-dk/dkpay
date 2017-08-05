from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
import random
import string
# Create your views here.
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.views.generic import ListView
from django.views.generic import TemplateView

from studygroup.models import StudyGroup, StudyGroupRule, StudyGroupMember,StudyGroupSession, StudyGroupDeposit

chars = string.ascii_lowercase + string.digits


def login(request):
    return TemplateResponse(request, 'layout_login.html')

@login_required
def accept_invitation(request):
    return TemplateResponse(request, 'layout_accept_invitation.html')


class MainView(TemplateView):
    template_name = 'layout_mygroups.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(MainView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data()
        study_groups = StudyGroup.objects.filter(studygroupmember__user=self.request.user)
        context['groups'] = study_groups
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
        admin = StudyGroupMember(
            group=group,
            user=request.user,
            is_admin=True
        )
        admin.save()

        group_id = str(group.id)

        absent_fee = request.POST.get('absent_fee')
        late_fee = request.POST.get('late_fee')
        default_deposit = request.POST.get('default_deposit')

        absent = StudyGroupRule(
            study_group=group,
            rule_name='absent',
            rule_amount=absent_fee
        )
        late = StudyGroupRule(
            study_group=group,
            rule_name='late',
            rule_amount=late_fee
        )
        deposit = StudyGroupRule(
            study_group=group,
            rule_amount=default_deposit,
            rule_name='deposit'
        )
        absent.save()
        late.save()
        deposit.save()

        return HttpResponse(group_id)


def create_group_result(request):
    if request.method == "GET":
        group = StudyGroup.objects.get(id=request.GET.get('id'))
        return render(request, 'layout_create_group_result.html', {'group': group})


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

    if request.method == "POST":
        absent_fee = request.POST.get('absent_fee')
        late_fee = request.POST.get('late_fee')
        default_deposit = request.POST.get('deposit')
        group_id = request.POST.get('id')
        group = StudyGroup.objects.get(id=group_id)

        absent = StudyGroupRule(
            group=group,
            rule_name='absent',
            rule_amount=absent_fee
        )
        late = StudyGroupRule(
            group=group,
            rule_name='late',
            rule_amount=late_fee
        )
        deposit = StudyGroupDeposit(
            study_group=group,
            name='default',
            amount=default_deposit
        )
        absent.save()
        late.save()
        deposit.save()
        return redirect('dashboard')


@login_required
def create_session(request, _id):
    if request.method == "GET":
        session = StudyGroupSession.objects.create(study_group_id=_id)
        members = User.objects.filter(studygroupmember__group_id=_id)
        return render(request, 'layout_edit_session.html', {'session':session,
                                                            'members': members})


@login_required
def edit_session(request, _id):
    if request.method == "GET":
        session = StudyGroupSession.objects.get(id=_id)
        members = User.objects.filter(studygroupmember__group_id=_id)
        return render(request, 'layout_edit_session.html', {'session':session,
                                                            'members':members})


class Dashboard(TemplateView):
    template_name = 'layout_group_dashboard.html'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(Dashboard, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        # group_id = self.request.GET.get('id')
        group_id = kwargs['id']
        study_group = StudyGroup.objects.get(id=group_id)

        context['study_group'] = study_group

        return context


class Session(ListView):
    template_name = 'layout_edit_session.html'
    model = StudyGroupMember

    def get_queryset(self, **kwargs):
        group_id = self.request.GET.get('id')
        qs_group_member = self.model.objects.filter(group_id=group_id)
        return qs_group_member


