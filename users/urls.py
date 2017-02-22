from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/citizen/$', views.req_citizen_profile, name='req_citizen_profile'),
]
