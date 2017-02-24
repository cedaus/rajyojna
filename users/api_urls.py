from django.conf.urls import url, include
import rest_views

urlpatterns = [
    url(r'^citizen/profile/$', rest_views.CitizenProfileView.as_view(), name='citizen_profile'),
    url(r'^citizen/login/aadhar/$', rest_views.CitizenLogin.as_view(), name='citizen_login_aadhar'),
    url(r'^citizen/signup/$', rest_views.CitizenSignup.as_view(), name='citizen_signup'),
]
