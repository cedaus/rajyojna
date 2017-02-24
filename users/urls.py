from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^citizen/profile/$', views.req_citizen_profile, name='req_citizen_profile'),
    url(r'^citizen/login/$', views.req_citizen_login, name='req_citizen_login'),
]
