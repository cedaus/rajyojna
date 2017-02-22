from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import models, serializers

class CitizenProfileView(APIView):
    print("I am citizen")
