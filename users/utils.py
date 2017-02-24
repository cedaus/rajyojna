from customauth.models import Citizen
from .models import CitizenProfile
import random

def create_citizen(first_name, last_name, aadhar_uid, password):
    username_unique = False
    username = first_name.lower().replace(" ", "") + str(random.randint(1, 999999))
    while not username_unique:
        try:
            Citizen.objects.get(username=username)
        except Citizen.DoesNotExist:
            username_unique = True

    first_name = first_name[0].upper() + first_name[1:].lower()
    last_name = last_name[0].upper() + last_name[1:].lower()

    citizen = Citizen.objects.create(username=username,aadhar_uid=aadhar_uid)
    citizen.save()
    citizen.set_password(password)
    citizen.save()
    citizen_profile = CitizenProfile.objects.create(citizen=citizen,first_name=first_name,last_name=last_name)

    return citizen, citizen_profile
