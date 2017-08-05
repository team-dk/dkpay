# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 12:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroupAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('current_balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MemberBlanace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MemberDepositTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_paid', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SessionChargeTable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_amount', models.IntegerField()),
                ('charge_descrip', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('link', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroupDeposit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('amount', models.IntegerField()),
                ('penalty_balance', models.IntegerField()),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroup')),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_admin', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroup')),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroupRule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rule_name', models.CharField(max_length=50)),
                ('rule_amount', models.IntegerField()),
                ('is_default', models.BooleanField(default=False)),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroup')),
            ],
        ),
        migrations.CreateModel(
            name='StudyGroupSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=40)),
                ('session_date', models.DateField()),
                ('session_time', models.TimeField()),
                ('study_group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroup')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('first_name', models.CharField(max_length=16)),
                ('last_name', models.CharField(max_length=16)),
                ('phone_number', models.IntegerField()),
                ('balance', models.IntegerField()),
                ('bank_account', models.CharField(max_length=40)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='studygroupmember',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.User'),
        ),
        migrations.AddField(
            model_name='sessionchargetable',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroupMember'),
        ),
        migrations.AddField(
            model_name='sessionchargetable',
            name='session',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroupSession'),
        ),
        migrations.AddField(
            model_name='memberdeposittable',
            name='deposit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroupDeposit'),
        ),
        migrations.AddField(
            model_name='memberdeposittable',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroupMember'),
        ),
        migrations.AddField(
            model_name='memberblanace',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroupMember'),
        ),
        migrations.AddField(
            model_name='groupaccount',
            name='study_group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='studygroup.StudyGroup'),
        ),
    ]