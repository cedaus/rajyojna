from django import forms
from django.contrib import admin
from .models import Citizen

from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField


class CitizenCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = Citizen
        fields = ['username', 'aadhar_uid', 'phone', 'email']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        citizen = super(CitizenCreationForm, self).save(commit=False)
        citizen.set_password(self.cleaned_data["password1"])
        if commit:
            citizen.save()
        return citizen


class CitizenChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = Citizen
        fields = ('email', 'password')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]

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
