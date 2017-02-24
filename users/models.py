from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import rajyojna.constants
import constants
from datetime import date


AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.User")
AUTH_CITIZEN_MODEL = 'customauth.Citizen'


class CitizenProfile(models.Model):
    citizen = models.OneToOneField(AUTH_CITIZEN_MODEL, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    sex = models.CharField(max_length=100, choices=constants.sex_choices)
    category = models.CharField(max_length=100, choices=constants.category_choices)
    language = models.CharField(max_length=100, choices=rajyojna.constants.language_choices)
    pan_num = models.CharField(max_length=10, unique=True, blank=True, default='NA', null=True)
    occupation = models.CharField(max_length=100, choices=constants.occupation_choices)
    education_status = models.CharField(max_length=100, choices=constants.education_status_choices)
    income_status = models.CharField(max_length=100, choices=constants.income_status_choices)
    birth = models.DateField(null=True, blank=True)
    death = models.DateField(null=True, blank=True)

    class Meta:
        verbose_name = "Citizen Profile"

    def __unicode__(self):
        return unicode(self.citizen.__unicode__())

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    @property
    def username(self):
        return self.citizen.username

    @property
    def aadhar_uid(self):
        return self.citizen.aadhar_uid

    @property
    def phone(self):
        return self.citizen.phone

    @property
    def email(self):
        return self.citizen.email

    """
    @property
    def age(self):
        return calculate_age(self.birth)

    @property
    def is_adult(self):
        if calculate_age(self.birth) >= 18:
            return True
        else:
            return False
    """

    def permanent_address(self):
        try:
            return CitizenAddress.objects.get(citizen_profile=self, permanent=True)
        except CitizenAddress.DoesNotExist:
            return None

    def bank_details(self):
        try:
            return CitizenBankProfile.objects.get(citizen_profile=self)
        except:
            return None

class CitizenAddress(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    citizen_profile = models.ForeignKey(CitizenProfile)
    address_line_1 = models.TextField(blank=True)
    address_line_2 = models.TextField(blank=True)
    landmark = models.TextField(blank=True)
    pin_code = models.IntegerField(null=True, blank=True)
    district = models.CharField(max_length=150, blank=True)
    state = models.CharField(max_length=100, choices=rajyojna.constants.states_in_india_choices, blank=True)
    country = models.CharField(max_length=50, default="INDIA", blank=True)
    permanent = models.BooleanField(default=False)
    current = models.BooleanField(default=False)
    verified = verified = models.BooleanField(default=False)

class CitizenBankDetail(models.Model):
    citizen_profile = models.OneToOneField(CitizenProfile)
    bank_account_name = models.CharField(max_length=150, blank=True)
    bank_account_number = models.CharField(max_length=150, blank=True)
    bank_ifsc = models.CharField(max_length=150, blank=True)
    verified = verified = models.BooleanField(default=False)


class DepartmentProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    full_name = models.TextField()
    short_name = models.CharField(max_length=150, blank=True)

class GovOfficerProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    officer = models.OneToOneField(AUTH_USER_MODEL, unique=True)
    department = models.ForeignKey(DepartmentProfile)
    @property
    def full_name(self):
        return self.officer.first_name + " " + self.officer.last_name

    @property
    def first_name(self):
        return self.officer.first_name

    @property
    def last_name(self):
        return self.officer.last_name

    @property
    def email(self):
        return self.officer.email

    @property
    def username(self):
        return self.officer.email
