# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-24 19:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20170225_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizenprofile',
            name='pan_num',
            field=models.CharField(blank=True, default='NA', max_length=10, null=True, unique=True),
        ),
    ]
