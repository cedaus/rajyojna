# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-23 13:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20170223_1857'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizenprofile',
            name='first_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='citizenprofile',
            name='last_name',
            field=models.CharField(default=2, max_length=100),
            preserve_default=False,
        ),
    ]
