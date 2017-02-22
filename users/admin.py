from .models import CitizenProfile, CitizenAddress, CitizenBankDetail, GovOfficerProfile
from django.contrib import admin

class CitizenAddressInline(admin.StackedInline):
    model = CitizenAddress
    extra = 0

class CitizenBankDetailInline(admin.StackedInline):
    model = CitizenBankDetail
    extra = 0

class CitizenProfileAdmin(admin.ModelAdmin):
    list_display = ['uid', 'username', 'first_name', 'last_name', 'email']
    inlines = [ CitizenAddressInline, CitizenBankDetailInline ]

    def uid(self, obj):
        return obj.citizen.id

    def username(self, obj):
        return obj.citizen.username

    def first_name(self, obj):
        return obj.citizen.first_name

    def last_name(self, obj):
        return obj.citizen.last_name

    def email(self, obj):
        return obj.citizen.email

admin.site.register(CitizenProfile, CitizenProfileAdmin)
