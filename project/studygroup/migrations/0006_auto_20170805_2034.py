# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 20:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studygroup', '0005_auto_20170805_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studygroupsession',
            name='session_date',
            field=models.DateField(auto_now=True),
        ),
    ]
