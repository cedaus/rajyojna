from django.contrib import admin
from .models import CitizenProfile, GovOfficerProfile

# Register your models here.
admin.site.register(CitizenProfile)
admin.site.register(GovOfficerProfile)
