from django.shortcuts import get_object_or_404
from rajyojna.utils import get_value_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from customauth.models import Citizen
from .models import CitizenProfile
from django.contrib.auth import authenticate

import models, serializers
from .utils import create_citizen

#Right your views here...
class CitizenLogin(APIView):
    def post(self, request, format=None):
        aadhar_uid = int(get_value_or_404(request.data, 'aadhar_uid'))
        password = get_value_or_404(request.data, 'password')
        try:
            citizen = authenticate(aadhar_uid=aadhar_uid, password=password)
        except Citizen.DoesNotExist:
            return Response('Invalid Login Method', status=status.HTTP_400_BAD_REQUEST)
        if citizen is None:
            return Response('Invalid Aadhar Id or Password', status=status.HTTP_400_BAD_REQUEST)
        return Response('success', status=status.HTTP_200_OK)

class CitizenSignup(APIView):
    def put(self, request, format=None):
        aadhar_uid = get_value_or_404(request.data, 'aadhar_uid')
        first_name = get_value_or_404(request.data, 'first_name')
        last_name = get_value_or_404(request.data, 'last_name')
        password = get_value_or_404(request.data, 'password')

        try:
            Citizen.objects.get(aadhar_uid=aadhar_uid)
            return Response('Citizen with the following details exist', status=status.HTTP_400_BAD_REQUEST)
        except Citizen.DoesNotExist:
            pass
        except Citizen.MultipleObjectsReturned:
            return Response('Some Error', status=status.HTTP_400_BAD_REQUEST)

        citizen, citizen_profile = create_citizen(first_name, last_name, aadhar_uid, password)

        return Response('success', status=status.HTTP_200_OK)

"""
clas CitizenUsername(APIView):

class CitizenPhone(APIView):


class CitizenEmail(APIView):
    def put(self, request, format=None):
        email = get_value_or_404(request.data, 'email')

        try:
            Citizen.objects.get(email=email)
            return Response('Citizen with the following details exist', status=status.HTTP_400_BAD_REQUEST)
        except Citizen.DoesNotExist:
            pass
        except Citizen.MultipleObjectsReturned:
            return Response('Some Error', status=status.HTTP_400_BAD_REQUEST)

"""
class CitizenProfileView(APIView):
    def get(self, request, format=None):
        print('')

    def put(self, request, format=None):
        print('')

    def post(self, request, format=None):
        print('')
