from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^registrationapi/$', views.registrationapi,name="registrationapi"),
    url(r'^$', views.booking,name="booking"),
]