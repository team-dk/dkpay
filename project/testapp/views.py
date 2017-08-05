from django.shortcuts import render

# Create your views here.
from django.template.response import TemplateResponse


def login(request):
    return TemplateResponse(request, 'login.html')

def accept_invitation(request):
    return TemplateResponse(request, 'accept_invitation.html')

def account_page_for_admin(request):
    return TemplateResponse(request, 'account_page_for_admin.html')

def create_group(request):
    return TemplateResponse(request, 'create_group.html')

def create_group_result(request):
    return TemplateResponse(request, 'create_group_result.html')

def deposit(request):
    return TemplateResponse(request, 'deposit.html')

def edit_admin_list(request):
    return TemplateResponse(request, 'edit_admin_list.html')

def edit_group(request):
    return TemplateResponse(request, 'edit_group.html')

def edit_session(request):
    return TemplateResponse(request, 'edit_session.html')

def group_dashboard(request):
    return TemplateResponse(request, 'group_dashboard.html')

def group_setting_for_admin(request):
    return TemplateResponse(request, 'group_setting_for_admin.html')

def my_groups(request):
    return TemplateResponse(request, 'mygroups.html')

def withdraw(request):
    return TemplateResponse(request, 'withdraw.html')
