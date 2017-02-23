from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import date


class CitizenManager(BaseUserManager):
     def create_citizen(self, username, aadhar_uid, password):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        if not aadhar_uid:
            raise ValueError('The given aadhar uid must be set')
        citizen = self.model(username=username,aadhar_uid=aadhar_uid,is_active=True,last_login=now,last_updated=now,date_created=now)
        citizen.set_password(password)
        citizen.save(using=self._db)
        return citizen


class Citizen(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    aadhar_uid = models.IntegerField(unique=True)
    phone = models.IntegerField(null=True, blank=True, unique=True)
    email = models.EmailField(max_length=255, null=True, blank=True, unique=True)
    aadhar_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    #is_authenticated = models.BooleanField(default=False)
    is_authorized = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    signup_done = models.BooleanField(default=False, blank=True)
    signup_stage = models.IntegerField(null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    last_login = models.DateTimeField(null=True, blank=True)
    last_update = models.DateTimeField(null=True, blank=True)
    date_deleted = models.DateTimeField(null=True, blank=True)
    login_count = models.IntegerField(null=True, blank=True)
    update_count = models.IntegerField(null=True, blank=True)

    objects = CitizenManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'aadhar_uid']

    class Meta:
        verbose_name = ('citizen')
        verbose_name_plural = ('citizens')
