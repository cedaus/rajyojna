from django.conf.urls import url, include
import rest_views

urlpatterns = [
    url(r'^profile/citizen/$', rest_views.CitizenProfileView.as_view(), name='citizen_profile'),
]
