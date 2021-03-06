# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-02-22 15:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20170222_2021'),
    ]

    operations = [
        migrations.CreateModel(
            name='CitizenBankDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_account_name', models.CharField(blank=True, max_length=150, null=True)),
                ('bank_account_number', models.CharField(blank=True, max_length=150, null=True)),
                ('bank_ifsc', models.CharField(blank=True, max_length=150, null=True)),
                ('verified', models.BooleanField(default=False)),
                ('citizen_profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.CitizenProfile')),
            ],
        ),
        migrations.RemoveField(
            model_name='citizenbankdetails',
            name='citizen_profile',
        ),
        migrations.AlterField(
            model_name='citizenaddress',
            name='address_line_1',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='citizenaddress',
            name='address_line_2',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='citizenaddress',
            name='country',
            field=models.CharField(blank=True, default='INDIA', max_length=50),
        ),
        migrations.AlterField(
            model_name='citizenaddress',
            name='landmark',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='citizenaddress',
            name='state',
            field=models.CharField(blank=True, choices=[(b'Andhra Pradesh', b'AP'), (b'Andaman and Nicobar Islands', b'AN')], max_length=100),
        ),
        migrations.DeleteModel(
            name='CitizenBankDetails',
        ),
    ]
