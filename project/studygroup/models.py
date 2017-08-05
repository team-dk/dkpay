from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name=None, last_name=None, report_email=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            report_email=report_email,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(max_length=16, null=False)
    last_name = models.CharField(max_length=16, null=False)
    phone_number = models.IntegerField(null=False)
    balance = models.IntegerField()
    bank_account = models.CharField(max_length=40)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.first_name

    def get_full_name(self):
        return self.last_name+' '+self.first_name


class StudyGroup(models.Model):
    name = models.CharField(max_length=40, null=False)
    link = models.CharField(max_length=40)


class StudyGroupRule(models.Model):
    study_group = models.ForeignKey(StudyGroup)
    rule_name = models.CharField(max_length=50, null=False)
    rule_amount = models.IntegerField()
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
    session_name = models.CharField(max_length=40, null=False)
    session_date = models.DateField()
    session_time = models.TimeField()


class SessionChargeTable(models.Model):
    session = models.ForeignKey(StudyGroupSession)
    member = models.ForeignKey(StudyGroupMember)
    charge_amount = models.IntegerField()
    charge_descrip = models.CharField(max_length=50, null=True)





