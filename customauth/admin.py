from django.contrib import admin
from .models import Citizen
from .forms import CitizenCreationForm, CitizenChangeForm

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class CitizenAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = CitizenChangeForm
    add_form = CitizenCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    fieldsets = [
        ('Credentials', {'fields': ('username', 'aadhar_uid', 'phone', 'email', 'password')}),
        ('Verifications', {'fields': ('aadhar_verified', 'phone_verified', 'email_verified')}),
        ('Sign Up', {'fields': ('signup_done', 'signup_stage',)}),
        ('Account Status', {'fields': ('is_authorized', 'is_active')}),
        ('Account Details', {'fields': ('last_login', 'login_count', 'last_update', 'update_count',)}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'aadhar_uid', 'password1', 'password2')}
        ),
    ]
    list_display = ['id', 'username', 'is_authorized', 'is_active', 'aadhar_uid', 'aadhar_verified', 'phone', 'phone_verified', 'email', 'email_verified', 'signup_done']
    search_fields = ['username', 'aadhar_uid']
    ordering = ['id',]
    list_filter = ()
    filter_horizontal = ()

# Register your models here.
admin.site.register(Citizen, CitizenAdmin)
