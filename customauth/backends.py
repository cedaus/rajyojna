from django.conf import settings
from django.contrib.auth.hashers import check_password
from .models import Citizen

class CitizenAuthBackend(object):
    def authenticate(self, aadhar_uid=None, password=None):
        try:
            citizen = Citizen.objects.get(aadhar_uid=aadhar_uid)
            if citizen.check_password(password):
                return citizen
        except Citizen.DoesNotExist:
            return None

    def get_citizen(self, username):
        try:
            citizen = Citizen.objects.get(username=username)
            if citizen.is_active:
                return citizen
            return None
        except Citizens.DoesNotExist:
            return None
