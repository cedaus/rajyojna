from .models import CitizenProfile, CitizenAddress, CitizenBankDetail, GovOfficerProfile
from django.contrib import admin

class CitizenAddressInline(admin.StackedInline):
    model = CitizenAddress
    extra = 0

class CitizenBankDetailInline(admin.StackedInline):
    model = CitizenBankDetail
    extra = 0

class CitizenProfileAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Citizen', {'fields': ('citizen',)}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'sex', 'birth', 'death')}),
        ('Cultural Info', {'fields': ('category', 'language',)}),
        ('Education Info', {'fields': ('education_status',)}),
        ('Business Info', {'fields': ('pan_num', 'occupation', 'income_status',)}),
    ]

    list_display = ['uid', 'first_name', 'last_name', 'sex', 'category', 'username', 'phone', 'email', 'is_authorized', 'is_active', 'signup_done']
    inlines = [ CitizenAddressInline, CitizenBankDetailInline ]

    def uid(self, obj):
        return obj.citizen.id

    def first_name(self, obj):
        return obj.first_name

    def last_name(self, obj):
        return obj.last_name

    def sex(self, obj):
        return obj.sex

    def category(self, obj):
        return obj.category

    def username(self, obj):
        return obj.citizen.username

    def phone(self, obj):
        return obj.citizen.phone

    def email(self, obj):
        return obj.citizen.email

    def is_authorized(self, obj):
        return obj.citizen.is_authorized

    def is_active(self, obj):
        return obj.citizen.is_active

    def signup_done(self, obj):
        return obj.citizen.signup_done

admin.site.register(CitizenProfile, CitizenProfileAdmin)
