from django.urls import path
from . import views

urlpatterns = [
    path("home/", views.index),
    path("xr/", views.xr_app, name='xr_form')
]