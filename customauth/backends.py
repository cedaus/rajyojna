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

    def get_user(self, user_id):
        try:
            citizen = Citizen.objects.get(pk=user_id)
            if citizen.is_active:
                return citizen
            return None
        except Citizen.DoesNotExist:
            return None
