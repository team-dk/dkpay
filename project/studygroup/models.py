from datetime import datetime
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import User


class StudyGroup(models.Model):
    name = models.CharField(max_length=40, null=False)
    link = models.CharField(max_length=40)
    passcode = models.CharField(max_length=8)


class StudyGroupRule(models.Model):
    study_group = models.ForeignKey(StudyGroup)
    rule_name = models.CharField(max_length=50, null=False)
    rule_amount = models.IntegerField(null=True)
    is_default = models.BooleanField(default=False)


class StudyGroupMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(StudyGroup, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)


class MemberBalance(models.Model):
    member = models.ForeignKey(StudyGroupMember)
    balance = models.IntegerField()


class GroupAccount(models.Model):
    study_group = models.ForeignKey(StudyGroup)
    current_balance = models.IntegerField()


class StudyGroupDeposit(models.Model):
    study_group = models.ForeignKey(StudyGroup)
    name = models.CharField(max_length=40, null=False)
    amount = models.IntegerField()
    penalty_balance = models.IntegerField()


class DepositTableManager(models.Manager):
    def create_deposit_list(self, study_group, deposit):
        member_list = StudyGroupMember.objects.filter(group=study_group)

        for member in member_list:
            new_deposit = self.model(
                member=member,
                deposit=deposit
            )
            new_deposit.save(self._db)


class MemberDepositTable(models.Model):
    deposit = models.ForeignKey(StudyGroupDeposit)
    member = models.ForeignKey(StudyGroupMember)
    is_paid = models.BooleanField(default=False)


class StudyGroupSession(models.Model):
    study_group = models.ForeignKey(StudyGroup)
    session_name = models.CharField(max_length=40, null=True)
    session_date = models.DateField(auto_now_add=True)
    session_time = models.TimeField(auto_now_add=True)


class SessionChargeTable(models.Model):
    session = models.ForeignKey(StudyGroupSession)
    member = models.ForeignKey(StudyGroupMember)
    charge_amount = models.IntegerField()
    charge_descrip = models.CharField(max_length=50, null=True)





