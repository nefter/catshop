"""Cats app URL config"""

from django.urls import path

from . import views


urlpatterns = [
    path('', views.cats, name='index'),
]
