from __future__ import unicode_literals
from django.conf import settings
from django.db import models
import rajyojna.constants
import constants
from datetime import date


AUTH_USER_MODEL = getattr(settings, "AUTH_USER_MODEL", "auth.Citizen")

class CitizenProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    citizen = models.OneToOneField(AUTH_USER_MODEL, unique=True)
    signup_done = models.BooleanField(default=False)
    signup_stage = models.IntegerField(default=1)
    email_verified = models.BooleanField(default=False)
    authorised = models.BooleanField(default=True)
    blocked = models.BooleanField(default=False)
    sex = models.CharField(max_length=100, choices=constants.sex_choices)
    category = models.CharField(max_length=100, choices=constants.category_choices)
    language = models.CharField(max_length=100, choices=rajyojna.constants.language_choices)
    pan_num = models.CharField(max_length=10, unique=True, blank=True)
    occupation = models.CharField(max_length=100, choices=constants.occupation_choices)
    education_status = models.CharField(max_length=100, choices=constants.education_status_choices)
    income_status = models.CharField(max_length=100, choices=constants.income_status_choices)
    birth = models.DateField()
    death = models.DateField(null=True, blank=True)

    class Meta:
        get_latest_by = "created"
        ordering = ['-created']
        verbose_name = "Citizen Profile"

    def __unicode__(self):
        return unicode(self.citizen.__unicode__())

    @property
    def full_name(self):
        return self.citizen.first_name + " " + self.citizen.last_name

    @property
    def first_name(self):
        return self.citizen.first_name

    @property
    def last_name(self):
        return self.citizen.last_name

    @property
    def email(self):
        return self.citizen.email

    @property
    def username(self):
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

    def aadhar_num(self):
        try:
            aadhar = CitizenAadhar.objects.get(citizen_profile=self).aadhar_uid
            return aadhar
        except CitizenAadhar.DoesNotExist:
            return None

    def aadhar_verified(self):
        try:
            verified = CitizenAadhar.objects.get(citizen_profile=self).verified
            return verified
        except CitizenAadhar.DoesNotExist:
            return False

    def primary_language(self):
        try:
            language = CitizenLanguage.objects.get(citizen_profile=self, primary=True).language
            return language
        except CitizenLanguage.DoesNotExist:
            return ''

    def primary_phone_number(self):
        try:
            phone_number = CitizenPhoneNumber.objects.get(citizen_profile=self, primary=True).phone_number
            return phone_number
        except CitizenPhoneNumber.DoesNotExist:
            return None

    def primary_phone_calling_code(self):
        try:
            return CitizenPhoneNumber.objects.get(citizen_profile=self, primary=True).calling_code
        except CitizenPhoneNumber.DoesNotExist:
            return None

    def primary_phone_verified(self):
        try:
            verified = CitizenPhoneNumber.objects.get(citizen_profile=self, primary=True).verified
            return verified
        except CitizenPhoneNumber.DoesNotExist:
            return False

    def permanent_address(self):
        try:
            return CitizenAddress.objects.get(citizen_profile=self, permanent=True)
        except CitizenAddress.DoesNotExist:
            return None

    def bank_details(self):
        try:
            return CitizenBankDetails.objects.get(citizen_profile=self)
        except:
            return None

class CitizenAadhar(models.Model):
    class Meta:
        get_latest_by = "created"
        ordering = ['-created']
        unique_together = ('citizen_profile', 'aadhar_uid')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    citizen_profile = models.ForeignKey(CitizenProfile)
    aadhar_uid = models.IntegerField(default=None)
    verified = models.BooleanField(default=False)

class CitizenPhoneNumber(models.Model):
    class Meta:
        get_latest_by = "created"
        ordering = ['-created']
        unique_together = ('citizen_profile', 'phone_number',)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    citizen_profile = models.ForeignKey(CitizenProfile)
    #uuid = UUIDField(auto=True, primary_key=True)
    phone_number = models.CharField(max_length=100)
    calling_code = models.CharField(max_length=10, default="91")
    verified = models.BooleanField(default=False)
    verification_uid = models.CharField(max_length=10, blank=True, null=True)
    primary = models.BooleanField(default=False)
    last_verified_at = models.DateTimeField(null=True, blank=True)

    def __unicode__(self):
        return unicode("(%s)%s"%(self.calling_code, self.phone_number))

class CitizenAddress(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    citizen_profile = models.ForeignKey(CitizenProfile)
    address_line_1 = models.TextField()
    address_line_2 = models.TextField()
    landmark = models.TextField()
    pin_code = models.IntegerField(blank=True)
    district = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=100, choices=rajyojna.constants.states_in_india_choices)
    country = models.CharField(max_length=50, default="INDIA")
    permanent = models.BooleanField(default=False)
    verified = verified = models.BooleanField(default=False)

class CitizenBankDetails(models.Model):
    citizen_profile = models.ForeignKey(CitizenProfile)
    bank_account_name = models.CharField(max_length=150, blank=True, null=True)
    bank_account_number = models.TextField(blank=True, null=True)
    bank_ifsc = models.TextField(blank=True, null=True)
    verified = verified = models.BooleanField(default=False)

class GovOfficerProfile(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    officer = models.OneToOneField(AUTH_USER_MODEL)
    department = models.ForeignKey()
    authorised = models.BooleanField(default=True)
    authorization_level = models.CharField(max_length=20, choices=constants.authorization_level_choices)
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
