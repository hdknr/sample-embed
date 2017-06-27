# coding: utf-8
from django.conf.urls import url
from django.contrib.auth import logout


urlpatterns = [
    url(r'^logout', logout, name='accounts_logout'),
]
